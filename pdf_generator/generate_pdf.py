from fpdf import FPDF

#Layout('P','L')
#Unit('mm','cm','in')
#format('A3','A4(default),'A5','Letter','Legal')
pdf=FPDF('P','mm','Letter')

pdf.add_page()

#fonts('times','courirt','helvetica','symbole')
# 'B'(bold) , 'U(underline) 'I'
pdf.set_font('times','U',16)

#W=width
#h=height

pdf.cell(40,10,"HELL YES ",ln=True)
pdf.cell(150,20,"bad bad ")

pdf.output('output_pdf.pdf')