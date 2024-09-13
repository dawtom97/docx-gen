from docx import Document

print("to jest MOJA ZMIANA!")

data = {
    "imie":"Barbara",
    "nazwisko":"Nowak",
    "punkty":"89",
    "firma":"Januszex"
}

def generate_docx(path):
    docx = Document(path)

    for paragraph in docx.paragraphs:
        for key, value in data.items():
            if f"{{{key}}}" in paragraph.text:
                paragraph.text = paragraph.text.replace(f"{{{key}}}", value)
    docx.save("nowy1.docx")

generate_docx("Certyfikat.docx")