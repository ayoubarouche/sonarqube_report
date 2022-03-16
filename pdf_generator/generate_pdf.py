from fpdf import FPDF
import datetime

#Layout('P','L')
#Unit('mm','cm','in')
#format('A3','A4(default),'A5','Letter','Legal')
pdf=FPDF('P','mm','Letter')

pdf.add_page()

#fonts('times','courirt','helvetica','symbole')
# 'B'(bold) , 'U(underline) 'I'
pdf.set_font('helvetica','B',30)


pdf.set_auto_page_break(auto=True,margin =15)
#W=width
#h=height
#ln=
#border=

pdf.cell(50)
pdf.ln(100)
pdf.cell(40)
pdf.cell(120,20,"Static Analysis Report ",ln=True,border=True,align='C')
pdf.set_font('times','I',20)
pdf.ln(10)
pdf.cell(0,10,"project title:" ,ln=20,align='C')
pdf.set_font('Arial','B',26)
pdf.set_text_color(250,50,50)
pdf.cell(0,20,"linux-prject",ln=True,align='C')
pdf.set_text_color(2,0,0)
datee=datetime.datetime.now()
print(str(datee))
pdf.set_font('times','U',12)
pdf.cell(0,60,str(datee),align='C')


pdf.output('output_pdf.pdf')