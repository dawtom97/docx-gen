from docx import Document
name=input("podaj imię: ")
surname=input("podaj nazwisko: ")
point=input("podaj ilość punktów: ")
company=input("podaj nazwę firmy: ")
data = {
    "imie":name,
    "nazwisko":surname,
    "punkty":point,
    "firma":company
}

def generate_docx(path):
    docx = Document(path)

    for paragraph in docx.paragraphs:
        for key, value in data.items():
            if f"{{{key}}}" in paragraph.text:
                paragraph.text = paragraph.text.replace(f"{{{key}}}", value)
    docx.save("nowy1.docx")

generate_docx("Certyfikat.docx")