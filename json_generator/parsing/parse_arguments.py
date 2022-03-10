import argparse
from unicodedata import name

from json_generator.models.branch import Branch
from json_generator.models.issue import Issue

from json_generator.models.project import Project

def entry_point_file(args):
    print("hello from the entry point file !")

def entry_point_cli(args):
    print("you choosed cli : ")
    if(args.project_branch and args.issues):
        parsing_results ={}
        if(args.token):
            print("you inserted the token and it's value is : "+args.token)
            parsing_results["auth"] = "t"

        elif(args.username and args.password):
            print("you inserted usename and password and it's value are : "+"username : "+args.username+" and it's password are : "+args.password)
            parsing_results["auth"] = "up"
        else :
            print("please enter the token or username and password (see help for more details !)")
            return None

        project_list = cli_parse_projects(args.project_branch)
        issues_list = cli_parse_issues(args.issues)
        for project in project_list:
            for branch in project.branches :
                branch.issues = issues_list
        parsing_results["projects"] = project_list 
        
        return parsing_results
    else :
        
        return None
#function to parse the arg of --project-branch

def cli_parse_projects(args):
    projects = args.split(',')
    projects_list = []
    for parsed_project in projects :
        projects_list.append(cli_parse_project(parsed_project))
    return projects_list
def cli_parse_project(project):
    
    project_branches = project.split(':')
    branches = cli_parse_branchs(project_branches[1])
    
    project_object = Project(key = project_branches[0],branches = branches)
    return project_object  
    
def cli_parse_branchs(branches):
    splited_branches = branches.split('#')
    branches_objects = []
    for splited_branch in splited_branches:
        branch = Branch(name=splited_branch)
        branches_objects.append(branch)
    return branches_objects

def cli_parse_issues(args):
    splitted_issues = args.split(',')
    issues_objects = []
    for issue in splitted_issues:
        issues_objects.append(Issue(key=issue))
    
    return issues_objects 
    



