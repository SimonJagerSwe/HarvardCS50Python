# Imports
from fpdf import FPDF

def main():
    shirt_printer("CS50 Shirtificate", input("Name: "), "shirtificate.png")


def shirt_printer(header, name, shirt):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", size=50)
    pdf.cell(0, 60, header, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.image(shirt, w=pdf.epw)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=47.5, y=140, text=f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()