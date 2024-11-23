from fpdf import FPDF
import re
import sys

class Name:
    def __init__(self, name=""):
        self.name = name

    def get_name(self):
        self.name = input("What's your name? ")
        if re.match(r'^[a-zA-Z ]+$', self.name):
            return self.name
        else:
            sys.exit('Input a valid name and last name.')

class Shirt:
    def __init__(self, name):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font('helvetica', 'B', 40)
        pdf.cell(0, 60, 'CS50 Shirtificate', align='C')
        pdf.image('shirtificate.png', x=0, y=70)
        pdf.set_font_size(20)
        pdf.set_text_color(255,255,255)
        pdf.text(x=60, y=140, txt=f"{name}'s shirtificate")
        pdf.output('shirtificate.pdf')

def main():
    name = Name()
    user_name = name.get_name()
    Shirt(user_name)

if __name__ == "__main__":
    main()
