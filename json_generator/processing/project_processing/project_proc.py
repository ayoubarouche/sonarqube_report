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

def append_to_jsonfile(data_filename,data):
    with open(data_filename, mode='w') as f:
        datafile=json.load(f)
    
    datafile.append(data)

    with open(data_filename, 'w') as json_file:
        json.dump(datafile, json_file, 
                        indent=4,  
                        separators=(',',': '))

#get proj 
def get_project(arg_proj):
    project=list(sonar.projects.search_projects(arg_proj.organization,arg_proj.key))
    tojson = json.dumps(project)
    Pr=arg_proj.parse_jsonProject(tojson)
    return Pr

def get_details_of_project(arg_proj):


    
def get_all_project(args_proj):
    for P in args_proj:
        json_format=get_project(P)
        

def get_branches_of_project(arg_proj):
    branches = sonar.project_branches.search_project_branches(arg_proj.key)
    json_obj=dumps(branches)
    Branchs=Branch()
    br=Branchs.parse_jsonbranch(json_obj)
    return br

def get_issues_of_project(arg_proj,args_branch):
    list_issue=[]
    for b in args_branch:
        issues =list(sonar.issues.search_issues(componentKeys=arg_proj.key, branch=b["branches"][0]["name"]))
        tojsonissue=json.dumps(issues)
        list_issue.append(tojsonissue)
    Issuee=Issue()
    obj_issues=[]
    for i in list_issue:
        iss=Issuee.parse_jsonissues(i)
        obj_issues.append(iss)
    return obj_issues
        

        




    





    


