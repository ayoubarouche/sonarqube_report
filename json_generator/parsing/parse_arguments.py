import argparse
from unicodedata import name


def entry_point_file(args):
    print("hello from the entry point file !")

def entry_point_cli(args):
    print("you choosed cli : ")
    if(args.project_branch):

        if(args.token):
            print("you inserted the token and it's value is : "+args.token)
            
        elif(args.username and args.password):
            print("you inserted usename and password and it's value are : "+"username : "+args.username+" and it's password are : "+args.password)
            
        project_list = cli_parse_projects(args.project_branch)
        for project in project_list:
            print(" the project name is : "+project.key)
    else :
        print("please enter the project and branch list ")
#function to parse the arg of -project-branch

def cli_parse_projects(args):
    projects = args.split(',')
    projects_list = []
    for parsed_project in projects :
        projects_list.insert(cli_parse_project(parsed_project))
    return projects_list
def cli_parse_project(project):
    
    project_branches = project.split(':')
    branches = cli_parse_branchs(project_branches[1])
    project_object = project(key = project_branches[0],branches = branches)
    return project_object  
    
def cli_parse_branchs(branches):
    splited_branches = branches.split('|')
    branches_objects = []
    for splited_branch in splited_branches:
        branch = Branch(name=splited_branch)
        branches_objects.insert(branch)
    return branches_objects



