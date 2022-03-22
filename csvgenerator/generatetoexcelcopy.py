import json
import csv
import pandas as pd 
import xlsxwriter
class ExcelFormatter:
    sheet = None
    book = None
    def __init__(self,project_name,workbook=None,current_row = 0 , current_column = 0 , formats = None  ) :
        self.workbook = workbook
        if not self.book:
            self.book = xlsxwriter.Workbook(project_name+".xlsx")
        self.current_row = current_row 
        self.current_column = current_column

        # check if the user inserted the formats or not : 

        #if the user inserted the formats 
        if formats : 
            self.formats = formats 
        else : 
            self.generate_default_format()

    def generate_default_format(self):
        #for the branch title format : 
        branch_title_format = self.book.add_format()
        branch_title_format.set_border(1)
        branch_title_format.set_bg_color("#F5DEB3") 
        branch_title_format.set_size(16)
        branch_title_format.set_align("center")
        branch_title_format.set_text_wrap()
        branch_title_format.set_align('center')
        branch_title_format.set_align('vcenter')
        branch_title_format.set_bold(True)
        #for the file title format : 
        file_title_format = self.book.add_format()
        file_title_format.set_border(1)
        file_title_format.set_bg_color("#edb39a") 
        file_title_format.set_size(16)
        file_title_format.set_align("center")
        file_title_format.set_text_wrap()
        file_title_format.set_align('center')
        file_title_format.set_align('vcenter')
        file_title_format.set_bold(True)
        #for the file infos format  :
        file_infos_format = self.book.add_format()
        file_infos_format.set_bg_color('#d9d964')
        file_infos_format.set_border(1)
        file_infos_format.set_align(alignment="center")
        file_infos_format.set_bold(True)

        # for the file details format : 
        file_details_format = self.book.add_format()

        file_details_format.set_bg_color("#FFFF99")

        file_details_format.set_border(style = 1)

        file_details_format.set_align('center')

        #for the issue details format 

        issue_details_format = self.book.add_format()
        issue_details_format.set_bg_color("#bcf2a5")
        issue_details_format.set_border(1)
        issue_details_format.set_text_wrap()
        issue_details_format.set_align('center')
        issue_details_format.set_align('vcenter')

        # for the issue infos format : 

        issue_infos_format = self.book.add_format()
        issue_infos_format.set_bg_color('#FFFF99')
        issue_infos_format.set_border(1)
        issue_infos_format.set_align("center")
        issue_infos_format.set_bold(True)
        #for the issue title format  : 

        issue_title_format = self.book.add_format()
        issue_title_format.set_bg_color("#d9d964")
        issue_title_format.set_border(1)
        issue_title_format.set_bold(True)
        issue_title_format.set_text_wrap()
        issue_title_format.set_align('center')
        issue_title_format.set_align('vcenter')


        #adding the formats :
        self.formats = {"file_title_format":file_title_format,
                    "file_header_format" : file_infos_format ,
                    "file_details_format" : file_details_format,
                    "issue_details_format" : issue_details_format,
                    "issue_infos_format" :issue_infos_format , 
                    "issue_title_format" :issue_title_format,
                    "branch_title_format":branch_title_format
                    }

    def add_sheet(self,branch_name = None):
        self.sheet = self.book.add_worksheet(branch_name)
    def add_issue(self , current_row , current_column , issue ):

    #add an author : 
        self.sheet.write(current_row , current_column , "Author",self.formats["issue_infos_format"])
        self.sheet.write(current_row , current_column+1 , issue.author, self.formats["issue_details_format"])
            #add a Tag : 
        self.sheet.write(current_row+1 , current_column , "Tag",self.formats["issue_infos_format"])
        self.sheet.write(current_row+1 , current_column+1 , str(issue.tags).replace("'","").replace("[","").replace("]",""), self.formats["issue_details_format"])
        
            #add an severity : 
        self.sheet.write(current_row+2, current_column , "Severity",self.formats["issue_infos_format"])
        self.sheet.write(current_row+2 , current_column+1 , issue.severity, self.formats["issue_details_format"])
        
            #add an category : 
        self.sheet.write(current_row+3, current_column , "Category",self.formats["issue_infos_format"])
        self.sheet.write(current_row+3 , current_column+1 , issue.type, self.formats["issue_details_format"])
        
                #add a creation date : 
        self.sheet.write(current_row+4, current_column , "Creation Date",self.formats["issue_infos_format"])
        self.sheet.write(current_row+4 , current_column+1, issue.creationDate, self.formats["issue_details_format"])
        
                #add a message : 
        self.sheet.write(current_row+5, current_column , "Message",self.formats["issue_infos_format"])
        self.sheet.write(current_row+5 , current_column+1 , issue.message , self.formats["issue_details_format"])
        

    def add_file(self, file_info,unresolved_issues=[] , wontfix_issues=[] , fixed_issues  = [], false_positive_isssues=[] , removed_issues=[]):
        if not self.sheet:
            print("error please create a sheet using create new sheet method ! ")
        number_of_issues = len(unresolved_issues) +len(wontfix_issues)+len(fixed_issues)+len(false_positive_isssues)+len(removed_issues)
        self.sheet.set_column(self.current_column , self.current_column , len("number of issues : "))
        self.sheet.set_row(self.current_row ,height = 25)


        file_name = file_info.name
        file_key = file_info.key
        file_uuid = file_info.uuid
        self.sheet.merge_range(self.current_row , self.current_column , self.current_row , self.current_column+1 , "File Details",self.formats["file_title_format"])
        self.current_row +=1
        #set the width of the column to the key length : 
        self.sheet.set_column(self.current_column+1 , self.current_column+1 , len(file_key))
        self.sheet.write(self.current_row , self.current_column , "file name " ,self.formats["file_header_format"] )
        self.sheet.write(self.current_row , self.current_column+1 , file_name , self.formats["file_details_format"])

        #for the file key : 

        self.sheet.write(self.current_row+1 , self.current_column , "file key",self.formats["file_header_format"] )
        self.sheet.write(self.current_row+1 , self.current_column+1 , file_key , self.formats["file_details_format"])
        
        # for the file uuid : 

        self.sheet.write(self.current_row+2 , self.current_column , "file uuid",self.formats["file_header_format"] )
        self.sheet.write(self.current_row+2 , self.current_column+1 , file_uuid, self.formats["file_details_format"])
        
        self.sheet.write(self.current_row+3 , self.current_column  , "number of issues : ",self.formats["file_header_format"] )
        self.sheet.write(self.current_row+3 , self.current_column+1 , number_of_issues, self.formats["file_details_format"])
        
        #adding issues : 
        new_current_row  = self.current_row+5 
        if unresolved_issues:
            
            self.sheet.merge_range(new_current_row , self.current_column , new_current_row , self.current_column+1 , "unresolved issues",self.formats["issue_title_format"])
            self.sheet.set_row(new_current_row ,height = 25)
            new_current_row+=1
            for issue in unresolved_issues:
                self.add_issue( current_row=new_current_row , current_column=self.current_column , issue = issue)
                new_current_row +=8
        #for fixed issues : 
        if wontfix_issues:
            self.sheet.merge_range(new_current_row , self.current_column , new_current_row , self.current_column+1 , "Wont Fix issues",self.formats["issue_title_format"])
            self.sheet.set_row(new_current_row ,height = 25)
            new_current_row+=1
            for issue in wontfix_issues:
                self.add_issue(current_row=new_current_row , current_column=self.current_column , issue = issue)
                new_current_row +=8

        #fixed issues 
        if fixed_issues:
            self.sheet.merge_range(new_current_row , self.current_column , new_current_row , self.current_column+1 , "Fixed issues",self.formats["issue_title_format"])
            self.sheet.set_row(new_current_row ,height = 25)
            new_current_row+=1
            for issue in fixed_issues:
                self.add_issue( current_row=new_current_row , current_column=self.current_column , issue = issue)
                new_current_row +=8

        # false positive issues :
        if false_positive_isssues:
            self.sheet.merge_range(new_current_row , self.current_column , new_current_row , self.current_column+1 , "False Positive issues")
            self.sheet.set_row(new_current_row ,height = 25)
            new_current_row+=1
            for issue in false_positive_isssues:
                self.add_issue(current_row=new_current_row , current_column=self.current_column , issue = issue)
                new_current_row +=8

        #for removed issues :
        if removed_issues:
            self.sheet.merge_range(new_current_row , self.current_column , new_current_row , self.current_column+1 , "Removed issues")
           
            new_current_row+=1
            for issue in removed_issues:
                self.add_issue( current_row=new_current_row , current_column=self.current_column , issue = issue)
                new_current_row +=8
        self.current_column+=4

    def branch_body(self,json_file):
        if self.sheet:
    #add branch column
            branch_name=json_file["branch-name"]
            self.sheet.merge_range(self.current_row-2,self.current_column,self.current_row+6,self.current_column,branch_name,self.formats["branch_title_format"])

            self.sheet.write(self.current_row+6,self.current_column+1,"Total",self.formats["file_header_format"])
            self.sheet.merge_range(self.current_row+6 , self.current_column+2 , self.current_row+6 , self.current_column+4 , json_file["unresolved-issues"]["total"],self.formats["file_header_format"])
            
            #add last-anaysis-date
            self.sheet.merge_range(self.current_row-2,self.current_column+1,self.current_row-2,self.current_column+2,"LastAnalysisDate",self.formats["issue_infos_format"])
            self.sheet.merge_range(self.current_row-2,self.current_column+3,self.current_row-2,self.current_column+4,json_file["date-Last-Analysis"],self.formats["issue_infos_format"])
            self.sheet.set_column(self.current_column , self.current_column , len("date-Last-Analysis"))
            self.sheet.set_column(self.current_column-2 , self.current_column+4 , len("date-Last-Analysis"))

            #Add category table
            dict_key1=json_file["unresolved-issues"]["issues-details"]["category"]
            dict_key2=json_file["unresolved-issues"]["issues-details"]["severity"]
            self.sheet.merge_range(self.current_row-1 , self.current_column+1 , self.current_row-1 , self.current_column+4 , "Summary Information",self.formats["file_title_format"])
            i=1
            for k in dict_key1.keys():

                self.sheet.write(self.current_row+i,self.current_column+1,k,self.formats["issue_details_format"])
                self.sheet.write(self.current_row+i,self.current_column+2,dict_key1[k],self.formats["issue_details_format"])
                i=i+1
            
            self.sheet.merge_range(self.current_row+4 , self.current_column+1 , self.current_row+5 , self.current_column+1 ,"security_hostpost",self.formats["issue_details_format"])
            self.sheet.merge_range(self.current_row+4 , self.current_column+2 , self.current_row+5 , self.current_column+2 ,dict_key1["security_hostpost"],self.formats["issue_details_format"])
            
            self.sheet.merge_range(self.current_row , self.current_column+1 , self.current_row , self.current_column+2 , "Category",self.formats["issue_title_format"])
            self.sheet.merge_range(self.current_row , self.current_column+3 , self.current_row , self.current_column+4 , "Severity",self.formats["issue_title_format"])

            j=1
            for k in dict_key2.keys():
                self.sheet.write(self.current_row+j,self.current_column+3,k,self.formats["issue_details_format"])
                self.sheet.write(self.current_row+j,self.current_column+4,dict_key2[k],self.formats["issue_details_format"])
                j=j+1


    def save_excel(self):
        self.book.close()


