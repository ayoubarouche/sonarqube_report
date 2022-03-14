from sonarqube import SonarCloudClient
from json_generator.models.branch import Branch
from json_generator.models.issue import Issue
from json_generator.models.project import Project
from json_generator.parsing.parse_arguments import cli_parse_projects, cli_parse_branchs,cli_parse_issues,cli_parse_project

import json 

# args_proj = cli_parse_projects(arg1)
# arg_proj=cli_parse_project(arg2)
# args_branch=cli_parse_branchs(arg3)
# args_issue=cli_parse_issues(arg4)

def show_error():
    print("Please enter a specific project ")

#parse class object to json String 
def parse_obj_to_json(class_obj):
    jsonStr = json.dumps(class_obj.__dict__)
    return jsonStr


def append_to_jsonfile(data_filename,data):
    with open(data_filename, mode='w') as f:
        datafile=json.load(f)
    
    datafile.append(data)

    with open(data_filename, 'w') as json_file:
        json.dump(datafile, json_file, 
                        indent=4,  
                        separators=(',',': '))

#get proj 
def get_project(sonar,arg_proj):
    project=list(sonar.projects.search_projects(organization=arg_proj.organization,projects=arg_proj.key))
    # tojson = json.dumps(project)
    # print(str(arg_proj.organization))
    Pr=arg_proj.parse_jsonProject(project[0])
    return Pr

# def get_details_of_project(sonar,arg_proj,args_branch,args_issue):
#     for B in args_branch:

    
def get_all_project(sonar,args_proj):
    for P in args_proj:
        object_format=get_project(P)
        

def get_branches_of_project(sonar,arg_proj):
    branches = list(sonar.project_branches.search_project_branches(arg_proj.key))
    Branchs=Branch(name=None)
    br=Branchs.parse_jsonbranch(branches)
    return br

def get_branches_of_all_projects(sonar,args_proj):
    branchesList=[]
    for P in args_proj:
        br=get_branches_of_project(sonar,P)
        branchesList.append(br)
    return branchesList

def get_issues_of_project(sonar,arg_proj,args_branch):
    list_issue=[]
    for b in args_branch:
        issues =list(sonar.issues.search_issues(componentKeys=arg_proj.key, branch=b.name))
        list_issue.append(issues)
    Issuee=Issue()
    obj_issues=[]
    for i in list_issue:
        iss=Issuee.parse_jsonissues(i)
        obj_issues.append(iss)
    return obj_issues

def get_issues_of_all_projects(sonar,args_proj,args_branch):
    object_list=[]
    for P in args_proj:
        issues_list=get_issues_of_project(sonar,P,args_branch)
        object_list.append(issues_list)
    return object_list

        
def get_spec_issues_of_project(sonar,arg_proj,args_branch,args_issue):
    listofissues=[]
    if args_branch:
        for b in args_branch:
            if args_issue :
                for i in args_issue:
                    issues=list(sonar.issues.search_issues(componentKeys=arg_proj.key, branch=b.name,tags=i.tags))
                    iss=Issue(key=None)
                    iss.parse_jsonissues(issues)
                    listofissues.append(iss)

    return listofissues     
    




        




    





    


