import re

class SpellReader(object):

    def __init__(self, page, cls):
        self._page = page
        self._cls = cls
        self.parts = []

    def parse(self):
        cleaned = self._clean()
        print(cleaned)
        #self._cls_from_text(cleaned)

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
            found = line.find(" {{bulletpoint}}")
            if(found>0):
                line = line.replace(" {{bulletpoint}}", "\n {{bulletpoint}}")
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

    def _cls_from_text(self, text):
        lines = text.splitlines()
        ln = lines.pop(0).strip()
        #class blocks start with free benefits.  Use this to grab the class name
        clsName = ln.replace(" FREE BENEFITS","").strip()
        #after this is a set of bullet-pointed benefits
        ln = lines.pop(0).strip()
        while "{{bulletpoint}}" in ln:
            self.freeBenefits.append(ln)
            ln = lines.pop(0).strip()
        #skills
        clsNameDoubleCheck = ln.replace(" SKILLS","").strip()
        if(clsName != clsNameDoubleCheck):
            print("class name and doublecheck don't match!")
            print('class name from free benefits: ',clsName)
            print('class name from skills: ',clsNameDoubleCheck)
            exit(1)
        self.className = clsName
        ln = lines.pop(0).strip()
        sk = None
        while "{{bulletpoint}}" not in ln:
            if re.search("^\*[A-Z ]+\*",ln):
                if sk is not None:
                    sk['text'] = " ".join(sk.pop('lines'))
                    self.skills.append(sk)
                (skill_name, max_select) = self._extract_skill_name(ln)
                sk = {"name": skill_name, "max_select": max_select, "lines": []}
            else:
                sk['lines'].append(ln)
            ln = lines.pop(0).strip()
        if sk is not None:
            self.skills.append(sk)
        print("done parsing class")

    def _extract_skill_name(self, line):
        if "{{skill-star}}" in line:
            match = re.search("\*([A-Z ]+)\* \(\{\{skill-star\}\}(.+)\)",line)
            return (match.group(1), match.group(2))
        else:
            return (line, 0)
        
    def _get_bold(self, text):
        match = re.search("^(\s*)([a-zA-Z0-9 ]+?)(\s*)$",text)
        if(match is not None):
            converted = f'{match.group(1)}*{match.group(2)}*{match.group(3)}'
            return converted
        else:
            return text



        

        
