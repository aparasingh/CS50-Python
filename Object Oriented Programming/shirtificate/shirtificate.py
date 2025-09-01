from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation='portrait')
pdf.add_page()
pdf.set_font('helvetica', size=40)
pdf.text(60, 30, "CS50 Shirtificate")
pdf.image("shirtificate.png", x=10, y=50, h=pdf.eph*0.75, w=pdf.epw)
pdf.output("shirtificate.pdf")
