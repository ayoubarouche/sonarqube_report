
"""
contains functions to handle and parse the config file : 
functions : 
    * entry_point_file : generale function to parse json config file 
    * parse_file : function to parse details from the config file  : 
    * auth_parser : function to parse the authentification method that the user want to use : token or login and password.
    * projects_parser : function to parser a project.
    * branches_parser : function to parse the branches specified by the user.
    * issues_parser : function to parse the issue tag list specified by the user.
"""
from os.path import exists
import json
from json_generator.models.branch import Branch
from json_generator.models.issue import Issue

from json_generator.models.project import Project 



def entry_point_file(file):

    #if the config file exist parse it 
    if(exists(file)):
        return parse_file(file)
    else :
        print("file not exist ! ")
        return None 

def parse_file(file):
    #open the json config file : 
    with open(str(file)) as json_file :
        json_object = json.load(json_file)
        json_file.close()
    
    result = {}
    #get the output file name : 
    # if the user specified the output file name : 
    if "output-filename" in json_object:
        result["output_filename"] = json_object["output-filename"]
    else : 

        result["output_filename"] = None
    #the organization name : required in case of sonarcloud : 
    if "organization" in json_object:
        result["organization"] = json_object["organization"]
    else :
        result["organization"] = "kestar"
 
    if 'sonarqube-url' in json_object and "authentication" in json_object:
        
        #parse the authentication method : 
        auth_method = auth_parser(json_object["authentication"])
        
        projects = None
        #parse the project object list  : 
        if "projects" in json_object : 
            projects = projects_parser(list(json_object["projects"]))

        # parse the sonarqube url : 
        sonarqube_url = json_object["sonarqube-url"]

        #in case of any error while parsing return NULL
        if not auth_method and not projects and not sonarqube_url: 
            return None

        #else fill the result dict and return it : 
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
        return None



def auth_parser(auth_dict):
    result={}
    #if the user inserted the token in the config file : 
    if "token" in auth_dict:
        result["auth"]= "t"
        result["token"]=auth_dict["token"]
        return result
    #if the user choosed the login and password method : 
    elif "username" and "password" in auth_dict:
        result["auth"] = "up"
        result["username"] = auth_dict["username"]
        result["password"] = auth_dict["password"]
        return result
    else :
        return None
def projects_parser(projects_dict):
    # if the user did not insert a list in the config file return NULL.
    if not isinstance(projects_dict,list) :
        return None
    else :
        project_list = []

        #run throw each project and parse it : 
        for project in projects_dict:
            project_object = None

            #if the user specified the project-key 
            if "project-key" in project: 
                project_object = Project(key=project["project-key"])
            else :
                return None

            #if the user specified the branch name : 
            if "branches" in project :
                project_branches = branches_parser(list(project["branches"]))
                project_object.branches = project_branches
            project_list.append(project_object)
        return project_list


def branches_parser(branches_dict):
    if not isinstance(branches_dict , list):
        return [Branch(name="master")]
    else :

        branches_list = []
        for branch in branches_dict:
            
            branch_object = None
            if "branch-name" in branch :
                branch_object = Branch(name = branch["branch-name"] )
            else :
                return None 
            #if the user inserted the issues tag list : 
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

