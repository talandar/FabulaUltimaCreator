import PyPDF2
import classReader
import spellReader

def parse_spells(text, dest_class):
    print(f"get spells for {dest_class['name']}")

with open("/shared/RPGs/FabulaUltima/Fabula_Ultima_TTJRPG.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)

    classes = {}
    spell_lists = {}

    number_of_pages = len(read_pdf.pages)
    for page_num in range(number_of_pages):
        page = read_pdf.pages[page_num]
        raw_text = page.extract_text()
        if(" SKILLS" in raw_text and " FREE BENEFITS" in raw_text):
            c_reader = classReader.ClassReader(page)
            parsed_class = c_reader.parse()
            classes[parsed_class['name']] = parsed_class
            print(f"got class {parsed_class['name']} from page {page_num}")
        for className in classes.keys():
            if f"{className} SPELLS" in raw_text:
                print(f'found spells on page {page_num} for class {className}, add next page to parse as well')
                spell_lists[page_num+1] = className
                sp_reader = spellReader.SpellReader(page,classes[className])
                sp_reader.parse()
        if page_num in spell_lists.keys():
            className = spell_lists[page_num]
            print(f'more spells for {className} on page {page_num}')
            sp_reader = spellReader.SpellReader(page,classes[className])
            sp_reader.parse()

    #print(classes)
    

