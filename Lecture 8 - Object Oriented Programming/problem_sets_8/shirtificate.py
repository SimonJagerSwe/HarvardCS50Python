# Imports
from fpdf import FPDF
from PIL import Image, ImageOps

def main():
    shirt = "shirtificate.png"
    shirt_printer("CS50 Shirtificate", input("Name: "), shirt)


def shirt_printer(header, name, shirt):
    pdf = FPDF(orientation="P", unit="mm", format=(210, 297))
    pdf.add_page()
    pdf.set_font("helvetica", size=24)
    pdf.image(shirt, 17, 67, 175)    
    pdf.cell(75, 50, name, align="C")
    pdf.cell(200, 200, header, align="C")    
    pdf.output("empty_test.pdf")

if __name__ == "__main__":
    main()