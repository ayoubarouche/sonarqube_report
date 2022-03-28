"""
contains functions for project processing and json manipulating files : 

functions : 
    * show_error : function that print a general error message 
    * parse_obj_to_json : function to convert a model to dict in case we want to generate the json format from a model object.
    * get_project : function to get a project details : 
    * get_branches_of_project : function to get all the branches of a project.
    * get_branches_of_all_project : function to get all the branches of all the projects
    * get_issues_of_project : function to get all issues in a project 
    * get_issues_of_all_project : function to get all issues of all projects
    * get_spec_issues_of_project : function to get issues of a specific tag list of a project.
    * 
"""

from json_generator.models.branch import Branch
from json_generator.models.issue import Issue



def show_error():
    print("Please enter a specific project ")

#parse class object to json String 
def parse_obj_to_json(class_obj):
    json_obj = vars(class_obj)
    
    return json_obj


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
    




        




    





    


