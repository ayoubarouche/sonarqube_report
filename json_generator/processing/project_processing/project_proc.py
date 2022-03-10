from sonarqube import SonarCloudClient
from json_generator.models.branch import Branch
from json_generator.models.issue import Issue
from json_generator.models.project import Project
from json_generator.parsing.parse_arguments import cli_parse_projects, cli_parse_branchs,cli_parse_issues,cli_parse_project

import json 

def show_error():
    print("Please enter a specific project ")


args_proj = cli_parse_projects(arg1)
arg_proj=cli_parse_project(arg2)
args_branch=cli_parse_branchs(arg3)
args_issue=cli_parse_issues(arg4)

#get proj 
def get_project(arg_proj):
    project=list(sonar.projects.search_projects(arg_proj.organization))
    tojson = json.dumps(project)
    return tojson

def append_to_jsonfile(data_filename,data):
    with open(data_filename, mode='w') as f:
        datafile=json.load(f)
    
    datafile.append(data)

    with open(data_filename, 'w') as json_file:
        json.dump(datafile, json_file, 
                        indent=4,  
                        separators=(',',': '))

    
def get_all_project(args_proj):
    for P in args_proj:
        json_format=get_project(P)
        jsonfile=open("json_file","w")
        append_to_jsonfile(jsonfile,json_format)
    
    return jsonfile






    


