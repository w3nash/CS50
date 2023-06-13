from fpdf import FPDF


class Shirtificate(FPDF):
    def template(self, name):
        self.add_page()
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw)
        self.set_font_size(30)
        self.set_text_color(255, 255, 255)
        text_width = self.get_string_width(name)
        self.text(x=(155 - text_width) / 2, y=140, txt=f"{name} took CS50")
        self.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    pdf = Shirtificate(orientation="P", format="A4", unit="mm")
    pdf.template(name)


if __name__ == "__main__":
    main()
