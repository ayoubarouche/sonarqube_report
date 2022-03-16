from pdf_generator.Body import PdfFormatter
from fpdf import FPDF
import datetime
# from pdf_generator.suumarytoPDF import summaryintoPDF

#Layout('P','L')
#Unit('mm','cm','in')
#format('A3','A4(default),'A5','Letter','Legal')
pdf=PdfFormatter('P','mm','A4')


pdf.first_page()
pdf.ln(20)
# pdf.add_page()
pdf.set_auto_page_break(auto=True,margin =15)
pdf.second_page('output_file.json')


pdf.output("output2_pdf.pdf")
