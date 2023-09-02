from fpdf import FPDF

pdf = FPDF()

def name():
    return input("Name: ").strip().title()

def main():
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=100, w=190, h=0, type='', link='')
    pdf.set_auto_page_break(False,0)
    name_param = name()
    add_name(name_param)
    add_title()
    pdf.output("shirtificate.pdf")

def add_title():
    title = "CS50 Shirtificate"
    pdf.set_font("Helvetica", "B" ,size=50)
    pdf.set_text_color(r=0,g=0,b=0)
    text_width = pdf.get_string_width(title)
    x_coordinate = pdf.w / 2 - (text_width / 2)
    y_coordinate = pdf.h / 8
    pdf.set_xy(x_coordinate, y_coordinate)
    pdf.set_xy(x_coordinate, pdf.y)
    pdf.cell(text_width, pdf.h/2-100, title, border=0, ln=1, align="C")

def add_name(name_param):

    tshirt_text = name_param + " took CS50"
    pdf.set_font("Helvetica", "B" ,size=25)
    pdf.set_text_color(r=255,g=255,b=255)
    text_width = pdf.get_string_width(tshirt_text)
    x_coordinate = pdf.w / 2 - (text_width / 2)
    pdf.set_xy(x_coordinate, pdf.y)
    pdf.cell(text_width, pdf.h/2+150, tshirt_text, border=0, ln=1, align="C")


if __name__ == "__main__" :
    main()