# Imports
from fpdf import FPDF
from PIL import Image, ImageOps

def main():
    shirt = "shirtificate.png"
    shirt_printer("CS50P", input("Name: "), shirt)


def shirt_printer(header, name, shirt):
    pdf = FPDF(orientation="P", unit="mm", format=(210, 297))
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=16)
    pdf.image(shirt, 17, 100, 175)    
    # pdf.cell()
    # pdf.cell(50, 50, header, align="C")    
    pdf.output("empty_test.pdf")

if __name__ == "__main__":
    main()