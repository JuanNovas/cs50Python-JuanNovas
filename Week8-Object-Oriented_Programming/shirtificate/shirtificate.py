from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF()
pdf.add_page(orientation="portrait")
pdf.set_font("helvetica", "B", 25)
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_text_color(0,0,0)
pdf.cell(0,30,"CS50 Shirtificate", align="C")
pdf.set_text_color(255,255,255)
pdf.cell(-200,250,f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")

