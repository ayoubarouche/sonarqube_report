#generating the header file : 

from fpdf import FPDF 


class PdfFormatter(FPDF):
    def header(self):
        self.image('images/lear_logo.png' ,
        10 ,
        8,
        60 )
        self.set_font('helvetica','B',20)
        self.ln(20)


