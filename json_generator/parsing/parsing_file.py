
from os.path import exists
import json
from json_generator.models.branch import Branch
from json_generator.models.issue import Issue

from json_generator.models.project import Project 


def entry_point_file(file):
    print("the file path is : "+file)
    print("hello from the entry point file !")
    if(exists(file)):
        return parse_file(file)
    else :
        print("file not exist : ")
        return None 

def parse_file(file):
    with open(str(file)) as json_file :
        json_object = json.load(json_file)
        json_file.close()
    
    result = {}
    if "organization" in json_object:
        result["organization"] = json_object["organization"]
    else :
        result["organization"] = "kestar"
    if 'sonarqube-url' and "projects" and "authentication" in json_object:
        auth_method = auth_parser(json_object["authentication"])
        projects = projects_parser(list(json_object["projects"]))
        sonarqube_url = sonarqube_parser(json_object["sonarqube-url"])
        if not auth_method and not projects and not sonarqube_parser: 
            return None
        else : 
            result["auth"] = auth_method["auth"]
            if(result["auth"]=="t"):
                result["token"] = auth_method["token"]
            elif(result["auth"]=="up"):
                result["username"] = auth_method["username"]
                result["password"]= auth_method["password"]
            result["projects"] = projects
            result["sonarqube_url"] = sonarqube_url
            result["issues"] = None
            return result
    else : 
        print("error parsing the json file please verify it !!")

    

    for project in projects : 
        print("the branches are : ")
        print(project['branches'])


def auth_parser(auth_dict):
    result={}
    if "token" in auth_dict:
        result["auth"]= "t"
        result["token"]=auth_dict["token"]
        return result

    elif "username" and "password" in auth_dict:
        result["auth"] = "up"
        result["username"] = auth_dict["username"]
        result["password"] = auth_dict["password"]
        return result
    else :
        return None
def projects_parser(projects_dict):
   
    if not isinstance(projects_dict,list) :
        return None
    else :
        project_list = []
        for project in projects_dict:
            project_object = None
            if "project-key" in project: 
                project_object = Project(key=project["project-key"])
            else :
                return None
            if "branches" in project :
                project_branches = branches_parser(list(project["branches"]))
                project_object.branches = project_branches
            project_list.append(project_object)
        return project_list

def sonarqube_parser(sonarqube_dict):
    return sonarqube_dict

def branches_parser(branches_dict):
    if not isinstance(branches_dict , list):
        return None
    else :

        branches_list = []
        for branch in branches_dict:
            
            branch_object = None
            if "branch-name" in branch :
                branch_object = Branch(name = branch["branch-name"] )
            else :
                return None 
            if "issues" in branch :
                branch_issues = issues_parser(list(branch["issues"]))
                branch_object.issues = branch_issues
            branches_list.append(branch_object)
        return branches_list   

def issues_parser(issues_dict):
    if not isinstance(issues_dict,list):
        return None
    else : 
        issue = Issue(key=None , tags = issues_dict)
        return [issue]

