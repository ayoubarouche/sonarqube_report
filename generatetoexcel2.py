
import json
import csv
import argparse
from json_generator.models.issue import Component
from json_generator.processing.issue_processing.parsing_component import parse_list_json_issues_to_list_json_objects
import xlsxwriter
import pandas as pd 
#function to add a file : 


def add_issue(sheet, current_row , current_column , issue):

    #add an author : 
    sheet.write(current_row , current_column , "Author")
    sheet.write(current_row , current_column+1 , issue.author)
        #add a Tag : 
    sheet.write(current_row+1 , current_column , "Tag")
    sheet.write(current_row+1 , current_column+1 , issue.tag)
    
        #add an severity : 
    sheet.write(current_row+2, current_column , "Severity")
    sheet.write(current_row+2 , current_column+1 , issue.severity)
    
        #add an category : 
    sheet.write(current_row+3, current_column , "Category")
    sheet.write(current_row+3 , current_column+1 , issue.type)
    
            #add a creation date : 
    sheet.write(current_row+4, current_column , "Creation Date")
    sheet.write(current_row+4 , current_column+1, issue.creationDate)
    
            #add a message : 
    sheet.write(current_row+5, current_column , "Message")
    sheet.write(current_row+5 , current_column+1 , issue.message)
    

def add_file(sheet , current_row , current_column , file_info,unresolved_issues=[] , wontfix_issues=[] , fixed_issues  = [], false_positive_isssues=[] , removed_issues=[]):
        number_of_issues = len(unresolved_issues) +len(wontfix_issues)+len(fixed_issues)+len(false_positive_isssues)+len(removed_issues)

        file_name = file_info.name
        file_key = file_info.key
        file_uuid = file_info.uuid

        sheet.write(current_row , current_column , "file name ")
        sheet.write(current_row , current_column+1 , file_name)

        #for the file key : 

        sheet.write(current_row+1 , current_column , "file key")
        sheet.write(current_row+1 , current_column+1 , file_key )
        
        # for the file uuid : 

        sheet.write(current_row+2 , current_column , "file uuid")
        sheet.write(current_row+2 , current_column+1 , file_uuid)
        
        sheet.write(current_row+3 , current_column  , "number of issues : ")
        sheet.write(current_row+3 , current_column+1 , number_of_issues)
        
        #adding issues : 
        new_current_row  = current_row+5 
        if unresolved_issues:
            new_current_row+=1
            for issue in unresolved_issues:
                add_issue(sheet=sheet , current_row=new_current_row , current_column=current_column)
                new_current_row +=8
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
current_column = 0 
s = book.add_worksheet("master") 
print("number of files is : "+str(len(files)))
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
    
    add_file(sheet =s , current_column=current_column , current_row=0 , file_info = file , unresolved_issues=unresolved_issues)
    current_column+=5
    
           
book.close()


