import json
from sys import stdin
import sys
import os
from excel_generator.generatetoexcel import ExcelFormatter
from json_generator.processing.issue_processing.parsing_component import parse_list_json_issues_to_list_json_objects
from pdf_generator.generatetopdf import PdfFormatter
from json_generator.models.component import Component
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process some integers")

    parser.add_argument("-f","--file",metavar="", required=False , dest="file", help="insert the sonarqube server url ")
    #get the output files direcotry 
    relative_path = "sonarqube-reports/"


    # get the script file : 

    script_dir = os.path.dirname(__file__)


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
        output = relative_path+project_name+'/'
        abs_file_path = os.path.join(script_dir ,output)
        is_exist = os.path.exists(abs_file_path)
        if not is_exist:
            os.makedirs(abs_file_path)
        # for the pdf : 
        # for excel :
        print("generating excel file for the project : "+project_name)

        
        for branch in project["details"]:
            excel = ExcelFormatter(abs_file_path+project_name+"_"+branch["summary_informations"]["branch-name"],None,0,0)
            #create measures titles :
            measures_titles = ["ncloc","comment_lines_density","complexity","cognitive_complexity"]
            
            #create a new sheet in the excel project name : 
            excel.add_sheet(sheet_name="summary informations")

            excel.branch_body(branch["summary_informations"],measures_titles=measures_titles)
            excel.add_sheet("measures")
            excel.add_header_title("measures",2,5)
            
            excel.add_sheet("issues")
            excel.move_by(1,2)
            #check if title of the files already added : 
            is_title_already_added = False
            for f in branch["information_per_file"]:
                file = Component(key=None)
                file.parse_jsoncomponent_from_output_file(f)
                issues_json = f["issues"]
                unresolved,wontfix = None,None
                if 'unresolved' in issues_json :
                    unresolved = list(issues_json["unresolved"])
                # print("the unresolved are : "+json.loads(str(unresolved[0]))["key"])
                if 'wontfix' in issues_json:
                    wontfix = list(issues_json["wontfix"])

                unresolved_issues = parse_list_json_issues_to_list_json_objects(unresolved)
                wontfix_issues = parse_list_json_issues_to_list_json_objects(wontfix)
                
                # add to excel : 
                #choose the title to add : 
                issue_titles = ['line','rule','status','resolution','severity','author','tags','comments']
                if not is_title_already_added:
                    excel.add_titles(issue_titles)
                    is_title_already_added = True
                excel.add_file(file ,issue_titles ,  unresolved_issues=unresolved,wontfix_issues=wontfix )
             
            #swl wach najotiw les tags tahoma ola blach 
            excel.save_excel()


    #