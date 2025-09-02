from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation='portrait')
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.set_font('helvetica', size=40)
pdf.cell(text="CS50 Shirtificate", h=40, w=200, align='C')
pdf.ln(110)
pdf.image("shirtificate.png", x=10, y=55, h=pdf.eph*0.75, w=pdf.epw)
pdf.set_font('helvetica', size=20)
pdf.set_text_color(r=255, g=255, b=255)
tshirt_text = name + " took CS50"
pdf.cell(text=tshirt_text, w=200, align='C')
pdf.output("shirtificate.pdf")
