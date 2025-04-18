from xhtml2pdf import pisa

with open("reservations.pdf", "wb") as pdf_file, open("reservations.html",encoding="utf-8") as html_file:
    pisa.CreatePDF(html_file.read(), dest=pdf_file)