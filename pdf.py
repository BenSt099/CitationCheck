from fpdf import FPDF

# Certain parts of the code taken from the documentation:
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

class PDF_REPORT(FPDF):
    def header(self):
        self.image('logo.png', 76, 11, 8, link='https://github.com/BenSt099/CitationCheck')
        self.set_font('Times', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'CitationCheck', 0, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def create_pdf_and_save(filename, data):
    # data = [
    # [entry1],[entry2],[entry3]
    #]
    # [entry1] = [Title, DOI, [Reasons]]

    filename = filename + ".pdf"

    pdf = PDF_REPORT()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    for i in range(0,len(data)):
        pdf.set_font('Times', 'B', 16)
        pdf.set_text_color(222, 53, 65)
        # pdf.set_fill_color(222, 53, 65)
        # pdf.cell(0, 10, data[i][0], 0, 1, fill=True)
        pdf.cell(0, 10, data[i][0], 0, 1)
        pdf.set_font('Times', '', 12)
        pdf.set_text_color(0,0,0)
        pdf.cell(0, 6, data[i][1], 0, 1)
        pdf.cell(0, 6, data[i][2], 0, 1)
        pdf.cell(0, 6, '', 0, 1)

    pdf.output(filename, 'F')


# ll = []
# ll.append(["Value1", "10020/32840987023", "Reason1; Reason2"])    
# ll.append(["Value2", "10020/328443534587023", "Reason1; Reason2"])    
# ll.append(["Value3", "10020/328404355555555555555345345023", "Reason1; Reason2"])    

# create_pdf_and_save('./example',ll)