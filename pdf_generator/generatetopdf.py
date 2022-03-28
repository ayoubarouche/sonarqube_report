#generating the header file : 

import datetime
from fpdf import FPDF 

title='Summary Information'

class PdfFormatter(FPDF):
    def header(self):
        self.image('images/lear_logo.png' ,
        10 ,
        8,
        60 )
        self.set_font('helvetica','B',20)
        self.ln(20)
    
    def body_of_first_page(self,jsonfile=None):
        # self.add_page()
       
        self.set_font('helvetica','B',30)
        self.set_auto_page_break(auto=True,margin =15)
        #W=width
        #h=height
        #ln=
        #border=
        self.cell(50)
        self.ln(60)
        self.cell(40)
        self.cell(120,20,"Static Analysis Report ",ln=True,border=True,align='C')
        self.set_font('times','I',20)
        self.ln(10)
        self.cell(0,10,f'project title:' ,ln=20,align='C')
        self.set_font('Arial','B',26)
        self.set_text_color(250,50,50)
        self.cell(0,20,f'{jsonfile["project_name"]}',ln=True,align='C')
        self.set_text_color(2,0,0)
        datee=datetime.datetime.now()
        self.set_font('times','U',12)
        self.cell(0,60,str(datee),align='C')


    def first_page(self,jsonfile):
        self.add_page()
        self.header()
        self.body_of_first_page(jsonfile=jsonfile)
        self.ln(50)

    def summaryHeader(self,title=title):

        self.set_font('helvetica', 'B', 15)
        title_w = self.get_string_width(title) + 6
         # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
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

    def TitlesHeader(self,title=title):

        self.set_font('helvetica', 'B', 15)
        title_w = self.get_string_width(title) + 6
         # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_draw_color(1, 1, 1) # border = blue
        self.set_fill_color(204, 204, 204) # background = yellow
        self.set_text_color(0, 0, 0) # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=False, ln=1, align='C', fill=1)
        # Line break
        self.ln(10)   

    def secondaryHeader(self,title=title):

        self.set_font('Arial', 'B', 15)
         # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_fill_color(255, 255, 255) # background = yellow
        self.set_text_color(0, 0, 0) # text = red
        # Thickness of frame (border)
        # self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=0, ln=1, align='C', fill=1)
        # Line break
        self.ln(10) 

    def branch_body(self,json_file):
    
        self.set_font('times', 'B', 12)
        space1 = self.get_string_width(title) + 10
        space2 = self.get_string_width("Last Analysis Date") +20
        self.set_line_width(0.5)
        # insert text
        self.cell(30)
        self.multi_cell(space1, 10, f'The branch name is : {json_file["branch-name"]}')
        self.cell(30)
        self.multi_cell(100, 10, f'Last Analysis Date : {json_file["date-Last-Analysis"]}')
        self.cell(30)
        self.multi_cell(100, 10, f'Total Unresolved Issues : {json_file["unresolved-issues"]["total"]}')
        self.cell(50)
        self.cell(130,10," ***** Statistics of unresolved issues by Category *****",ln=1)
        self.set_font('times', '', 12)
        self.cell(50)
        self.cell(space2, 10, f'Code Smell' , border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["category"]["code_smell"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Bugs' , border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["category"]["Bug"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Vulnerability' , border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["category"]["vulerability"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Security Hostpost' , border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["category"]["security_hostpost"]}',border='BRT',align='C')
        self.cell(50)
        self.set_font('times', 'B', 12)
        self.cell(130,10," ***** Statistics of unresolved issues by Severity *****",ln=1)
        self.set_font('times', '', 12)
        self.cell(50)
        self.cell(space2, 10, f'Major', border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["severity"]["MAJOR"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Minor', border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["severity"]["MINOR"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Critical', border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["severity"]["CRITICAL"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f' Info', border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["severity"]["INFO"]}',border='BRT',align='C')
        self.cell(50)
        self.cell(space2, 10, f'Blocker', border=1,align='C')
        self.set_font('times', '', 12)
        self.multi_cell(50,10,f'{json_file["unresolved-issues"]["issues-details"]["severity"]["BLOCKER"]}',border='BRT',align='C')

    def second_page(self,json_file,first_page = False):
        if first_page:
            self.add_page()
        self.ln(20)
        self.summaryHeader()
        self.branch_body(json_file)
        self.ln(60)

    def add_issue(self , issue):
            self.set_line_width(0.3)
            self.ln(0.5)
            self.set_font('times', '', 12)

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
        self.set_font('times', '', 12)
        name = self.get_string_width('number_of_issues') + 10
        # insert text
        self.cell(name, 10, f'File name' , border=1)
        self.multi_cell(self.w-name-20 , 10 , file_name,border='BRT',align='C')
        self.set_font('times', '', 12)

        self.cell(name, 10, f'File key',border=1)
        self.multi_cell(self.w-name-20 , 10 , file_key,border='BRT',align='C')
        self.cell(name, 10, f'File Uuid',border=1)
        self.multi_cell(self.w-name-20 , 10 , file_uuid,border='BRT',align='C')
        self.cell(name, 10, f'number of issues',border=1)
        self.multi_cell(self.w-name-20 , 10 , str(number_of_issues),border='BRT',align='C')
        self.ln(10)

        self.secondaryHeader(title="**Issues details**")
        self.cell(50)
        self.set_x(15)
        i = 1
        #for unresolved issues : 
        if unresolved_issues:
            self.cell(10 )
            self.set_font('times', 'B', 12)
            self.cell(130,10,f"{i}) Unresolved Issues",ln=1)
            i +=1
            for issue in unresolved_issues:
                self.add_issue(issue)
        #for fixed issues : 
        if wontfix_issues:
            self.cell(10 )
            self.set_font('times', 'B', 12)

            self.cell(130,10,f"{i}) Wontfix Issues",ln=1)
            i +=1
            for issue in wontfix_issues:
                self.add_issue(issue)

        #fixed issues 
        if fixed_issues:
            self.cell(10 )
            self.set_font('times', 'B', 12)

            self.cell(130,10,f"{i}) Fixed Issues",ln=1)
            i +=1
            for issue in fixed_issues:
                self.add_issue(issue)

        # false positive issues :
        if false_positive_isssues:
            self.cell(10 )
            self.set_font('times', 'B', 12)

            self.cell(130,10,f"{i}) False Positive Issues",ln=1)
            i +=1
            for issue in false_positive_isssues:
                self.add_issue(issue)

        #for removed issues :
        if removed_issues:
            self.cell(10 )
            self.cell(130,10,f"{i}) Removed Issues",ln=1)
            i +=1
            for issue in removed_issues:
                self.add_issue(issue)
    
    



