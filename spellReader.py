import re

class SpellReader(object):

    def __init__(self, page, cls):
        self._page = page
        self._cls = cls
        self.parts = []

    def parse(self):
        cleaned = self._clean()
        spells = self._to_spells(cleaned)
        #print(f'cleaned spell text for class {self._cls["name"]}')
        #print(cleaned)
        if('spells' in self._cls):
            self._cls['spells'] = self._cls['spells'] + spells
        else:
            self._cls['spells'] = spells


    def _clean(self):
        self._page.extract_text(visitor_text=self._spell_visitor)
        text = "".join(self.parts)

        # extra cleanup here
        lines = text.splitlines()
        cleanedParts = []
        for line in lines:
            line = line.replace("{{skill-star}}{{skill-star}}","{{skill-star}}")
            line = line.replace("{{attackspell}}{{attackspell}}","{{attackspell}}")
            line = line.replace("*T erra*","*Terra*")
            line = line.replace("*T orpor*","*Torpor*")
            line = line.replace("cc Spells marked with {{attackspell}} are *offensive spells* and require *Magic Checks*!",'')
            line = line.replace(" 】","】")
            line = line.replace("【 ","【")
            found = line.find(" {{bulletpoint}}")
            if(found>0):
                line = line.replace(" {{bulletpoint}}", "\n {{bulletpoint}}")
            if(re.match("^\d+$",line.strip())):
                #page number
                continue
            if("SPELL MP TARGET DURATION" in line.strip()):
                #header
                continue
            if(f"WW{self._cls['name']} SPELLS" in line.strip()):
                #header
                continue
            cleanedParts.append(line)
        text = '\n'.join(cleanedParts)
        return text


    def _spell_visitor(self, text, cm, tm, fontDict, fontSize):
        baseFont = "" if fontDict is None else fontDict['/BaseFont']
        x_pos = tm[4]
        y_pos = tm[5]
        if(text and x_pos>=0.1 and y_pos>=0.1 and x_pos<=375):
            if('Wingdings' in baseFont):
                if(text=='w'):
                    self.parts.append("{{bulletpoint}}")
                elif(text=='ç'):
                    self.parts.append("{{skill-star}}")
                else:
                    self.parts.append("[wingdings "+text+"]")
            elif('oldretrolabelstfb' in baseFont):
                self.parts.append(f"[retrolabels: {text}]")
            elif('Heydings-Icons' in baseFont):
                if(text=='r' or text==' r'):
                    self.parts.append("{{attackspell}}")
                else:
                    self.parts.append(f"[heydings {text}]")
            elif('Bold' in baseFont):
                if(text.isspace()):
                    self.parts.append(text)
                else:
                    self.parts.append(self._get_bold(text))
            else:
                self.parts.append(text)

    def _to_spells(self, text):
        lines = text.splitlines()
        spells = []
        spell = None
        while(len(lines)>0):
            ln = lines.pop(0).strip()
            if(ln.endswith("Instantaneous") or ln.endswith("Scene")):
                #finished parsing old spell
                if(spell is not None):
                    spell['text'] = " ".join(spell.pop('lines'))
                    spells.append(spell)
                spell = self._parse_spell_title_line(ln)
            else:
                spell['lines'].append(ln)
        #out of text, but we have a spell left to add to the list
        spell['text'] = " ".join(spell.pop('lines'))
        spells.append(spell)
        return spells
                    
    def _parse_spell_title_line(self, line):
        spell = {}
        name = line[0:(line.index('*',1)+1)]
        spell['name'] = name
        spell['attack'] = ("{{attackspell}}" in line)
        if("Instantaneous" in line):
            spell['duration'] = 'Instantaneous'
        else:
            spell['duration'] = 'Scene'
        line = line.replace(name,"")
        line = line.replace("{{attackspell}}","")
        line = line.replace('Instantaneous','')
        line = line.replace('Scene','')
        line = line.strip()
        #should be down to "(cost) (targets)"
        match = re.match('^(up to \d+)|^(\d+ × T)|^(\d+)',line)
        cost = match.group(0)
        spell['cost'] = cost
        line = line.replace(cost,'').strip()
        spell['targets'] = line
        spell['lines'] = []
        return spell
        #spells start with *(NAME)* (opt {{attackspell}}) (cost) (targets) (Instantaneous/Scene)
        
    def _get_bold(self, text):
        match = re.search("^(\s*)([a-zA-Z0-9 ]+?)(\s*)$",text)
        if(match is not None):
            converted = f'{match.group(1)}*{match.group(2)}*{match.group(3)}'
            return converted
        else:
            return text



        

        
