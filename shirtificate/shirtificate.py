from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation = 'P', format = 'A4')
pdf.add_page()
pdf.set_font("helvetica", "B", 50)
pdf.cell(0, 60, "CS50 Shirtificate", align = 'C')
pdf.image('shirtificate.png', x= 5, y = 70, h = 210, w = 200)
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(r = 255, g = 255, b = 255)
pdf.text(x=47.5, y=140, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")