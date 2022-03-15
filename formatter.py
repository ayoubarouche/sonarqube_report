from pdf_generator.header import PdfFormatter



pdf = PdfFormatter('P', 'mm' , 'Letter')

pdf.set_auto_page_break(
    auto=True , margin=15
)


pdf.add_page()

pdf.output('report.pdf')