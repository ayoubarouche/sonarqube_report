import json
from sys import stdin
import sys
from unittest import expectedFailure
from csvgenerator.generatetoexcel import ExcelFormatter
from json_generator.processing.issue_processing.parsing_component import parse_list_json_issues_to_list_json_objects
from pdf_generator.Body import PdfFormatter
from json_generator.models.issue import Component
import argparse

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


for project in data :
    project_name= project["project_name"]
    # for the pdf : 
    pdf = PdfFormatter('P', 'mm' , 'Letter')
    # for excel :
    excel = ExcelFormatter(project_name,None,3,0)
    pdf.set_auto_page_break(
        auto=True , margin=15
    )
    print('the pdf is : '+str(pdf.w))


    #print data for each file : 
    pdf.first_page(project)
    pdf.ln(20)
    # pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin =15)

    
    for branch in project["details"]:
        #create a new sheet in the excel project name : 
        excel.add_sheet(branch_name=branch["summary_informations"]["branch-name"])
        i=1
        if i==1:
            pdf.second_page(branch["summary_informations"],True)
        else :
            pdf.second_page(branch["summary_informations"])
        pdf.summaryHeader(title='General view of the files')
        excel.branch_body(branch["summary_informations"])
        for f in branch["information_per_file"]:
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
            #add to the pdf : 
            pdf.TitlesHeader(title='File Number : '+str(i))
            pdf.add_file(file , unresolved_issues=unresolved_issues,wontfix_issues=wontfix_issues ,fixed_issues=fixed_issues , false_positive_isssues=false_positive_issues , removed_issues=removed_issues)
            # add to excel : 
            excel.add_file(file , unresolved_issues=unresolved_issues,wontfix_issues=wontfix_issues ,fixed_issues=fixed_issues , false_positive_isssues=false_positive_issues , removed_issues=removed_issues)
            i=i+1
            pdf.ln(20)
        #swl wach najotiw les tags tahoma ola blach 
    excel.save_excel()
    pdf.output(project_name+'.pdf')


#