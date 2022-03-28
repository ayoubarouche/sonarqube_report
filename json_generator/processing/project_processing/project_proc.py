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
    json_obj = vars(class_obj)
    if isinstance(json_obj , Issue):
        json_obj["comments"] = class_obj.comments
    return json_obj



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
    if project :
        Pr=arg_proj.parse_jsonProject(project[0])
        return Pr
    return None
    

        

def get_branches_of_project(sonar,arg_proj):
    branches = sonar.project_branches.search_project_branches(arg_proj.key)
    brs=[]
    for b in branches['branches']:
        Branchs=Branch(name=None)
        Branchs.parse_jsonbranch(b)
        brs.append(Branchs)
    return brs

def get_branches_of_all_projects(sonar,args_proj):
    branchesList=[]
    for P in args_proj:
        br=get_branches_of_project(sonar,P)
        branchesList.append(br)
    return branchesList

def get_issues_of_project(sonar,arg_proj,args_branch):
    issues =list(sonar.issues.search_issues(componentKeys=arg_proj.key, branch=args_branch.name,additionalFields="comments"))
    obj_issues=[]
    for i in issues:
        Issuee=Issue(key=None)
        Issuee.parse_jsonissues(i)
        obj_issues.append(Issuee)
    return obj_issues

def get_issues_of_all_projects(sonar,args_proj,args_branch):
    object_list=[]
    for P in args_proj:
        issues_list=get_issues_of_project(sonar,P,args_branch)
        object_list.append(issues_list)
    return object_list

        
def get_spec_issues_of_project(sonar,arg_proj,args_branch,args_issue):
    listofissues=[]
    result_issue_tags = ",".join(map(str, args_issue.tags))
    print("the issue sare : ")
    print(result_issue_tags)
    issues=list(sonar.issues.search_issues(componentKeys=arg_proj.key, branch=args_branch.name,tags=result_issue_tags,additionalFields="comments"))
    for i in issues:
        iss=Issue(key=None)
        iss.parse_jsonissues(i)
        listofissues.append(iss)
        print("the issue is : ")
        print(iss.key)
        print(iss.tags)

    return listofissues     
    




        




    





    


