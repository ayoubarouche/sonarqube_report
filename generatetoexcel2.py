
from email import header
import json
import csv
import argparse
from csvgenerator.generatetoexcel import ExcelFormatter
from json_generator.models.issue import Component
from json_generator.processing.issue_processing.parsing_component import parse_list_json_issues_to_list_json_objects
import xlsxwriter
import pandas as pd 
#function to add a file : 



parser = argparse.ArgumentParser(description="process some integers")

parser.add_argument("-f","--file",metavar="", required=False , dest="file", help="insert the sonarqube server url ")

args = parser.parse_args()
json_file = None
data = None
if args.file :
    
    json_file = open(args.file,'r')
    data = json.load(json_file)
else: 
    try:
        json_file = sys.stdin.readline()
        data = json.loads(str(json_file))
    except:
        print(str(json_file))
        print("error in the command !")
        exit()

files = data[0]["details"][1]["information_per_file"]

        # access to each file :
        # 
        # #creating the sheet for each branch : 
        # 


book = xlsxwriter.Workbook("output.xlsx")

#set the first column and the first row for the sheet : 
current_row = 2 
current_column = 1 
s = book.add_worksheet("master") 
print("number of files is : "+str(len(files)))

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

# for the file details format : 
file_details_format = book.add_format()

file_details_format.set_bg_color("#FFFF99")

file_details_format.set_border(style = 1)

file_details_format.set_align('center')

#for the issue details format 

issue_details_format = book.add_format()
issue_details_format.set_bg_color("#bcf2a5")
issue_details_format.set_border(1)
issue_details_format.set_text_wrap(True)

# for the issue infos format : 

issue_infos_format = book.add_format()
issue_infos_format.set_bg_color('#FFFF99')
issue_infos_format.set_border(1)
issue_infos_format.set_align("center")
issue_infos_format.set_bold(True)
#for the issue title format  : 

issue_title_format = book.add_format()
issue_title_format.set_bg_color("#d9d964")
issue_title_format.set_border(1)
issue_title_format.set_bold(True)
issue_title_format.set_text_wrap()
issue_title_format.set_align('center')
issue_title_format.set_align('vcenter')


#adding the formats :
formats = {"file_title_format":file_title_format,
            "file_header_format" : file_infos_format ,
            "file_details_format" : file_details_format,
            "issue_details_format" : issue_details_format,
            "issue_infos_format" :issue_infos_format , 
            "issue_title_format" :issue_title_format
             }

excel = ExcelFormatter("world" ,current_column=2 , current_row=2)

excel.add_sheet("master")

for f in files:
    file = Component(key=None)
    file.parse_jsoncomponent_from_output_file(f)
    issues_json = f["issues"]

    unresolved = list(issues_json["unresolved"])
            # print("the unresolved are : "+json.loads(str(unresolved[0]))["key"])

    wontfix = list(issues_json["wontfix"])

    fixed = list(issues_json["fixed"])

    false_positive = list(issues_json["false_positive"])

    removed = list(issues_json["removed"])

    unresolved_issues = parse_list_json_issues_to_list_json_objects(unresolved)
    wontfix_issues = parse_list_json_issues_to_list_json_objects(wontfix)
    fixed_issues = parse_list_json_issues_to_list_json_objects(fixed)
    false_positive_issues = parse_list_json_issues_to_list_json_objects(false_positive)
    removed_issues = parse_list_json_issues_to_list_json_objects(removed)
    
    excel.add_file(file_info = file , unresolved_issues=unresolved_issues , wontfix_issues= wontfix_issues , fixed_issues= fixed_issues , false_positive_isssues= false_positive_issues , removed_issues=removed_issues )
    current_column+=4
    
           
excel.save_excel()


