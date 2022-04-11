import xlsxwriter
class ExcelFormatter:
    sheet = None
    book = None
    default_row = 0
    default_column = 0
    def __init__(self,project_name,workbook=None,current_row = 0 , current_column = 0 , formats = None  ) :
        self.workbook = workbook
        if not self.book:
            self.book = xlsxwriter.Workbook(project_name+".xlsx")
        self.current_row = current_row 
        self.current_column = current_column
        self.default_row = self.current_row 
        self.default_column = self.current_column
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
 
        file_title_format.set_align("center")
        file_title_format.set_text_wrap()
        file_title_format.set_align('center')
        file_title_format.set_align('vcenter')
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

        #for the summary details format 

        summary_details_format = self.book.add_format()
        summary_details_format.set_bg_color("#bcf2a5")
        summary_details_format.set_border(1)
        summary_details_format.set_text_wrap()
        summary_details_format.set_align('center')
        summary_details_format.set_align('vcenter')

        # for the issue infos format : 

        issue_infos_format = self.book.add_format()
        issue_infos_format.set_bg_color('#FFFF99')
        issue_infos_format.set_border(1)
        issue_infos_format.set_align("center")

        #for the issue title format  : 

        issue_title_format = self.book.add_format()
        issue_title_format.set_bg_color("#d9d964")
        issue_title_format.set_border(1)
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
                    "branch_title_format":branch_title_format,
                    "summary_details_format":summary_details_format
                    }

    def add_sheet(self,sheet_name = None):
        self.sheet = self.book.add_worksheet(sheet_name)
        self.current_column = self.default_column
        self.current_row = self.default_row

    def reset_default_row_and_column(self,row=True , column = True):
        if column :
            self.current_column = self.default_column 
        if row : 
            self.current_row = self.default_row
    def add_issue(self , issue_headers,current_row , current_column , issue ):
        i = 0 
        for issue_header in issue_headers :
            #check if the value of the issue header is an array : 

            if isinstance(issue[issue_header] , list):
                #to manipulate a field : 
                    #manipulate the tags field 
                if issue_header == 'tags':
                    issue[issue_header] = str(issue[issue_header]).replace("'","").replace("[","").replace("]","")
                    
                    #manipulate the comments field :
                if issue_header == 'comments':
                    if issue[issue_header]: 
                        issue[issue_header] = issue[issue_header][-1]['htmlText']
                    else : 
                        issue[issue_header] = ""
                    

            self.sheet.write(current_row,current_column+i,str(issue[issue_header]),self.formats["issue_infos_format"])
            # self.sheet.write(self.current_row+i,self.current_column+2,dict_key1[k],self.formats["summary_details_format"])
            i=i+1
    def add_header_title(self,title,number_of_rows_to_merge=0 , number_of_column_to_merge=1):
        self.sheet.merge_range(self.current_row , self.current_column , self.current_row+number_of_rows_to_merge-1 , self.current_column+number_of_column_to_merge-1 , title,self.formats["file_title_format"])
            
        self.current_row+=(number_of_rows_to_merge-1)
        self.current_column+=(number_of_column_to_merge-1)
    def add_titles(self , issue_headers,add_issue_type=True , add_by_columns = True):
        if add_by_columns:
            self.current_column = self.default_column

            
            self.sheet.write(self.current_row , self.current_column , "file name" , self.formats["issue_details_format"])
            if add_issue_type:
                self.sheet.write(self.current_row , self.current_column+1 , "issue type",self.formats["issue_details_format"])

                self.current_column+=1
            self.sheet.set_column(self.current_column , self.current_column+len(issue_headers),25)

            i=1
            for issue_header in issue_headers:
                
                self.sheet.write(self.current_row,self.current_column+i,issue_header,self.formats["summary_details_format"])
                # self.sheet.write(self.current_row+i,self.current_column+2,dict_key1[k],self.formats["summary_details_format"])
                i=i+1
            self.current_row+=1
        if not add_by_columns:
            self.current_column = self.default_column

            self.sheet.set_column(self.current_column , self.current_column+2,25)
            i=1
            for issue_header in issue_headers:
                
                self.sheet.merge_range(self.current_row,self.current_column,self.current_row , self.current_column+1,issue_header,self.formats["summary_details_format"])
                # self.sheet.write(self.current_row+i,self.current_column+2,dict_key1[k],self.formats["summary_details_format"])
                self.current_row+=1
            self.current_row+=1
            
    
    def add_file(self, file_info,issue_headers,unresolved_issues=[] , wontfix_issues=[] , fixed_issues  = [], false_positive_isssues=[] , removed_issues=[]):
        if not self.sheet:
            print("error please create a sheet using create new sheet method ! ")
        self.current_column = self.default_column
        number_of_issues = len(unresolved_issues) +len(wontfix_issues)+len(fixed_issues)+len(false_positive_isssues)+len(removed_issues)
        # self.sheet.set_column(self.current_column , self.current_column , len("number of issues : "))
        # self.sheet.set_row(self.current_row ,height = 25)

        

        file_name = file_info.name
       # return to the default column : 
        self.current_column = self.default_column

        for i in range(number_of_issues) :
            self.sheet.write(self.current_row+i ,self.current_column , file_name, self.formats["file_title_format"])

       
        #adding issues : 
        
        if unresolved_issues:
            self.current_column+=1
            for i in range(len(unresolved_issues)):
                self.sheet.write(self.current_row+i ,self.current_column , "unresolved issue", self.formats["issue_title_format"])
            
            self.current_column+=1

            for issue in unresolved_issues:

                self.add_issue( current_row=self.current_row , current_column=self.current_column , issue = issue , issue_headers = issue_headers)
                self.current_row +=1
            self.current_column-=2

            
        #for fixed issues : 
        if wontfix_issues:
            self.current_column+=1

            for i in range(len(wontfix_issues)):
                self.sheet.write(self.current_row+i ,self.current_column , "wont-fix issue", self.formats["issue_title_format"])
            self.current_column+=1
            # new_current_row+=1
            for issue in wontfix_issues:

                self.add_issue( current_row=self.current_row , current_column=self.current_column , issue = issue , issue_headers = issue_headers)
                self.current_row +=1
            self.current_column-=2
    


    
    def branch_body(self,json_file , measures_titles = None):
        if self.sheet:
    #add branch column
            # branch_name=json_file["branch-name"]
            # # self.current_row+=2
            # self.sheet.merge_range(self.current_row,self.current_column,self.current_row+8,self.current_column,branch_name,self.formats["branch_title_format"])

            self.sheet.write(self.current_row+8,self.current_column+1,"Total",self.formats["file_header_format"])
            self.sheet.merge_range(self.current_row+8 , self.current_column+2 , self.current_row+8 , self.current_column+4 , json_file["unresolved-issues"]["total"],self.formats["file_header_format"])
            
            #Add category table
            dict_key1=json_file["unresolved-issues"]["issues-details"]["category"]
            dict_key2=json_file["unresolved-issues"]["issues-details"]["severity"]
            self.sheet.merge_range(self.current_row+1 , self.current_column+1 , self.current_row+1 , self.current_column+4 , "Summary Information",self.formats["file_title_format"])
            i=3
            for k in dict_key1.keys():

                self.sheet.write(self.current_row+i,self.current_column+1,k,self.formats["summary_details_format"])
                self.sheet.write(self.current_row+i,self.current_column+2,dict_key1[k],self.formats["summary_details_format"])
                i=i+1
            
            self.sheet.merge_range(self.current_row+6 , self.current_column+1 , self.current_row+7 , self.current_column+1 ,"security_hostpost",self.formats["summary_details_format"])
            self.sheet.merge_range(self.current_row+6 , self.current_column+2 , self.current_row+7 , self.current_column+2 ,dict_key1["security_hostpost"],self.formats["summary_details_format"])
            
            self.sheet.merge_range(self.current_row+2 , self.current_column+1 , self.current_row+2 , self.current_column+2 , "Category",self.formats["issue_title_format"])
            self.sheet.merge_range(self.current_row+2 , self.current_column+3 , self.current_row+2, self.current_column+4 , "Severity",self.formats["issue_title_format"])

            j=3
            for k in dict_key2.keys():
                self.sheet.write(self.current_row+j,self.current_column+3,k,self.formats["summary_details_format"])
                self.sheet.write(self.current_row+j,self.current_column+4,dict_key2[k],self.formats["summary_details_format"])
                j=j+1

            self.current_row+=12

            # adding measures of project : 
            
            self.add_measures_for_project(measures = json_file["measures"])
    
    
    def add_measures_for_project(self,  measures=None):
        self.add_header_title("project measures" , 0 , 4)
        self.reset_default_row_and_column(row=False)
        self.move_by(2)
        for measure in measures : 
            self.add_measure_for_project(measure)

    def add_measure_for_project(self , measure):

        self.sheet.merge_range(self.current_row,self.current_column,self.current_row , self.current_column+1,measure["metric"],self.formats["summary_details_format"])
        self.move_by(0 , 2)
        self.sheet.merge_range(self.current_row,self.current_column,self.current_row , self.current_column+1,measure["value"],self.formats["summary_details_format"])
        self.move_by(1 , -2)

    def move_by(self , number_of_rows_to_add=0 , number_of_columns_to_add=0):
        
        self.current_row += number_of_rows_to_add 
        self.current_column += number_of_columns_to_add
        
    def save_excel(self):
        self.book.close()


