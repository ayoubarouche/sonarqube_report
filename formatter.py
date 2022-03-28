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
        pdf = PdfFormatter('P', 'mm' , 'Letter')
        # for excel :
        excel = ExcelFormatter(abs_file_path+project_name,None,0,0)
        pdf.set_auto_page_break(
            auto=True , margin=15
        )
        print('generating pdf and excel files for the project : '+project_name)


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
                
                #add to the pdf : 
                pdf.TitlesHeader(title='File Number : '+str(i))
                pdf.add_file(file , unresolved_issues=unresolved_issues,wontfix_issues=wontfix_issues )
                # add to excel : 
                #choose the title to add : 
                issue_titles = ['line','rule','status','resolution','severity','author','tags','comments']
                if not is_title_already_added:
                    excel.add_titles(issue_titles)
                    is_title_already_added = True
                excel.add_file(file ,issue_titles ,  unresolved_issues=unresolved,wontfix_issues=wontfix )
                i=i+1
                pdf.ln(20)
            #swl wach najotiw les tags tahoma ola blach 
        excel.save_excel()


        pdf.output(abs_file_path+project_name+'.pdf')
        pdf.close()

    #