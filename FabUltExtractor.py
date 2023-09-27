import PyPDF2
import classReader
import spellReader

import json

classes = {}

with open("/shared/RPGs/FabulaUltima/Fabula_Ultima_TTJRPG.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)

    spell_lists = {}

    number_of_pages = len(read_pdf.pages)
    for page_num in range(number_of_pages):
        page = read_pdf.pages[page_num]
        raw_text = page.extract_text()
        if(" SKILLS" in raw_text and " FREE BENEFITS" in raw_text):
            c_reader = classReader.ClassReader(page)
            parsed_class = c_reader.parse()
            classes[parsed_class['name']] = parsed_class
        for className in classes.keys():
            if f"{className} SPELLS" in raw_text:
                spell_lists[page_num+1] = className
                sp_reader = spellReader.SpellReader(page,classes[className])
                sp_reader.parse()
        if page_num in spell_lists.keys():
            className = spell_lists[page_num]
            sp_reader = spellReader.SpellReader(page,classes[className])
            sp_reader.parse()

for cls in classes.values():
    with open(f"output_ignored/extracted_{cls['name']}.json",'wt') as output_json:
        json.dump(cls,output_json, indent = 2, ensure_ascii=False)
    

