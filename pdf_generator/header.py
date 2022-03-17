#generating the header file : 

import json
from fpdf import FPDF 


class PdfFormatter(FPDF):
    def header(self):
        self.image('images/lear_logo.png' ,
        10 ,
        8,
        60 )
        self.set_font('helvetica','B',20)
        self.ln(20)
    
    def summaryHeader(self,title):
        self.set_font('helvetica', 'B', 15)
        self.set_font('times', 'B', 12)
        title_w = self.get_string_width(title) + 6
         # Calculate width of title and position

        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_draw_color(1, 1, 1) # border = blue
        self.set_fill_color(255, 204, 204) # background = yellow
        self.set_text_color(0, 0, 0) # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
        # Line break
        self.ln(10)


    def add_issue(self , issue):
            self.set_line_width(0.3)
            self.ln(0.5)
 
            name = self.get_string_width('Creation Date') + 10
            self.cell(name, 10, f'Author' , border=1)
            self.multi_cell(self.w-name-20 , 10 , issue.author,border='BRT',align='C')
            self.cell(name, 10, f'Tag' , border=1)
            self.multi_cell(self.w-name-20 , 10 , str(issue.tags).replace("'","").replace("[","").replace("]",""),border='BRT',align='C')
            
            self.cell(name, 10, f'Severity',border=1)
            self.multi_cell(self.w-name-20 , 10 , issue.severity,border='BRT',align='C')
            self.cell(name, 10, f'Category',border=1)
            self.multi_cell(self.w-name-20 , 10 , issue.type,border='BRT',align='C')
            self.cell(name, 10, f'Creation Date',border=1)
            self.multi_cell(self.w-name-20 , 10 , issue.creationDate,border='BRT',align='C')
            self.cell(name, 10, f'Message ',border=1)
            self.multi_cell(self.w-name-20 , 10 , issue.message,border='BRT',align='C')
            
            self.ln(10)


    def add_file(self,file_info,unresolved_issues=[] , wontfix_issues=[] , fixed_issues  = [], false_positive_isssues=[] , removed_issues=[]):
        number_of_issues = len(unresolved_issues) +len(wontfix_issues)+len(fixed_issues)+len(false_positive_isssues)+len(removed_issues)
        self.set_line_width(0.5)
        file_name = file_info.name
        file_key = file_info.key
        file_uuid = file_info.uuid
        self.set_font('times', 'B', 12)
        name = self.get_string_width('number_of_issues') + 10
        # insert text
        self.cell(name, 10, f'File name' , border=1)
        self.multi_cell(self.w-name-20 , 10 , file_name,border='BRT',align='C')

        self.cell(name, 10, f'File key',border=1)
        self.multi_cell(self.w-name-20 , 10 , file_key,border='BRT',align='C')
        self.cell(name, 10, f'File Uuid',border=1)
        self.multi_cell(self.w-name-20 , 10 , file_uuid,border='BRT',align='C')
        self.cell(name, 10, f'number of issues',border=1)
        self.multi_cell(self.w-name-20 , 10 , str(number_of_issues),border='BRT',align='C')
        self.ln(10)

        self.summaryHeader(title='Details about issues')
        self.cell(50)
        self.set_x(15)
        i = 1
        #for unresolved issues : 
        if unresolved_issues:
            self.cell(10 )
            self.cell(130,10,f"{i}) Unresolved Issues",ln=1)
            i +=1
            for issue in unresolved_issues:
                self.add_issue(issue)
        #for fixed issues : 
        if wontfix_issues:
            self.cell(130,10,f"{i}) Wontfix Issues",ln=1)
            i +=1
            for issue in wontfix_issues:
                self.add_issue(issue)

        #fixed issues 
        if fixed_issues:
            self.cell(130,10,f"{i}) Fixed Issues",ln=1)
            i +=1
            for issue in fixed_issues:
                self.add_issue(issue)

        # false positive issues :
        if false_positive_isssues:
            self.cell(130,10,f"{i}) False Positive Issues",ln=1)
            i +=1
            for issue in false_positive_isssues:
                self.add_issue(issue)

        #for removed issues :
        if removed_issues:
            self.cell(130,10,f"{i}) Removed Issues",ln=1)
            i +=1
            for issue in removed_issues:
                self.add_issue(issue)
    