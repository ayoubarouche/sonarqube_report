import json
import csv
from operator import index
from unicodedata import category
import pandas as pd 
import openpyxl
import xlsxwriter


def branch_body(sheet,current_row,current_column,json_file,formats = None):
    #add branch column
    branch_name=json_file["branch-name"]
    sheet.merge_range(current_row-2,current_column,current_row+6,current_column,branch_name,formats["branch_title_format"])

    sheet.write(current_row+6,current_column+1,"Total",formats["file_header_format"])
    sheet.merge_range(current_row+6 , current_column+2 , current_row+6 , current_column+4 , json_file["unresolved-issues"]["total"],formats["file_header_format"])
    
    #add last-anaysis-date
    sheet.merge_range(current_row-2,current_column+1,current_row-2,current_column+2,"LastAnalysisDate",formats["issue_infos_format"])
    sheet.merge_range(current_row-2,current_column+3,current_row-2,current_column+4,json_file["date-Last-Analysis"],formats["issue_infos_format"])
    sheet.set_column(current_column-2 , current_column+2 , len(json_file["date-Last-Analysis"]))
    #Add category table
    dict_key1=json_file["unresolved-issues"]["issues-details"]["category"]
    dict_key2=json_file["unresolved-issues"]["issues-details"]["severity"]
    sheet.merge_range(current_row-1 , current_column+1 , current_row-1 , current_column+4 , "Summary Information",formats["file_title_format"])
    i=1
    for k in dict_key1.keys():

        sheet.write(current_row+i,current_column+1,k,formats["issue_details_format"])
        sheet.write(current_row+i,current_column+2,dict_key1[k],formats["issue_details_format"])
        i=i+1
  
    sheet.merge_range(current_row , current_column+1 , current_row , current_column+2 , "Category",formats["issue_title_format"])
    sheet.merge_range(current_row , current_column+3 , current_row , current_column+4 , "Severity",formats["issue_title_format"])

    j=1
    for k in dict_key2.keys():
        sheet.write(current_row+j,current_column+3,k,formats["issue_details_format"])
        sheet.write(current_row+j,current_column+4,dict_key2[k],formats["issue_details_format"])
        j=j+1
       

book = xlsxwriter.Workbook('outfile.xlsx')   # Creating Excel Writer Object from Pandas  
json_file = open("output_file.json",'r')
data = json.load(json_file)
worksheet_name=data[0]["details"][0]["summary_informations"]["branch-name"]
s=book.add_worksheet(worksheet_name+".json")
file=data[0]["details"][0]["summary_informations"]
# for the file details format : 
#adding the formats :

#for the branch title format : 
branch_title_format = book.add_format()
branch_title_format.set_border(1)
branch_title_format.set_bg_color("#F5DEB3") 
branch_title_format.set_size(16)
branch_title_format.set_align("center")
branch_title_format.set_text_wrap()
branch_title_format.set_align('center')
branch_title_format.set_align('vcenter')
branch_title_format.set_bold(True)

#for the file title format : 
file_title_format = book.add_format()
file_title_format.set_border(1)
file_title_format.set_bg_color("#edb39a") 
file_title_format.set_size(16)
file_title_format.set_align("center")
file_title_format.set_text_wrap()
file_title_format.set_align('center')
file_title_format.set_align('vcenter')
file_title_format.set_bold(True)

#for the file infos format  :
file_infos_format = book.add_format()
file_infos_format.set_bg_color('#d9d964')
file_infos_format.set_border(1)
file_infos_format.set_align(alignment="center")
file_infos_format.set_bold(True)

#for the issue details format 

issue_details_format = book.add_format()
issue_details_format.set_bg_color("#bcf2a5")
issue_details_format.set_border(1)
issue_details_format.set_text_wrap(True)

#for the issue title format  : 

issue_title_format = book.add_format()
issue_title_format.set_bg_color("#d9d964")
issue_title_format.set_border(1)
issue_title_format.set_text_wrap()
issue_title_format.set_align('center')
issue_title_format.set_align('vcenter')

 # for the issue infos format : 

issue_infos_format = book.add_format()
issue_infos_format.set_bg_color('#FFFF99')
issue_infos_format.set_border(1)
issue_infos_format.set_align("center")
issue_infos_format.set_bold(True)


formats = {"file_title_format":file_title_format,
            "branch_title_format":branch_title_format,
            "file_header_format" : file_infos_format ,
            # "file_details_format" : file_details_format,
            "issue_details_format" : issue_details_format,
            "issue_infos_format" :issue_infos_format , 
            "issue_title_format" :issue_title_format
            #  
            }
branch_body(s,2,0,file,formats)
book.close()