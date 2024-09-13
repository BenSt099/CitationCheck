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

        list_of_lines = format_title(data[i][0])
        for line in list_of_lines:
            pdf.cell(0, 7, line, 0, 1)
        pdf.set_font('Times', '', 12)
        pdf.set_text_color(0,0,0)
        pdf.cell(0, 6, data[i][1], 0, 1)

        list_of_reasons = format_reasons(data[i][2])
        for reason in list_of_reasons:
            reason = reason.strip()
            if reason != '':
                pdf.cell(20)
                pdf.cell(0, 6, reason, 0, 1)
        pdf.cell(0, 6, '', 0, 1)

    pdf.cell(0, 6, '', 0, 1)
    pdf.set_font('Times', 'I', 8)
    pdf.cell(0, 5, 'This report was generated using the Open-Source software "CitationCheck".', 0, 1, 'C')
    pdf.cell(0, 5, 'This report comes without any WARRANTY, without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.', 0, 1, 'C')
    pdf.output(filename, 'F')

def format_title(title):
    # MAX = 63 characters
    title_list = []
    oneline = ''
    if len(title) <= 63:
        title_list.append(title)
        return title_list
    sections = title.split(' ')
    for word in sections:
        if len(oneline) + len(word) <= 63:
            oneline = oneline + word + ' '
        else:
            title_list.append(oneline.strip())
            oneline = '' + word + ' '
    if oneline.strip() != '':
        title_list.append(oneline.strip())
    return title_list

def format_reasons(reasons):
    return reasons.split(';')