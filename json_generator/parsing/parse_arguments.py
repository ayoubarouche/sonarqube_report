"""
contains functions to parse the arguments from the command line : 
functions : 
    * entry_point_cli : generale function to parse args.
    * cli_parse_projects : function to parse the project argument.
    * cli_parse_branchs : function to parse the branch inserted by the user
    * cli_parse_issues : function to parse issue tag list inserted by the user.
"""
from json_generator.models.branch import Branch
from json_generator.models.issue import Issue

from json_generator.models.project import Project


def entry_point_cli(args):
    
    #if the user specified the project names and the sonarqube server url.
    if(args.sonarqube_url):
        parsing_results ={}

        #if the user passed -t argument : 
        if(args.token):
            parsing_results["auth"] = "t"
            parsing_results["token"] = args.token
            
        #if the user passed the login and username arguments
        elif(args.username and args.password):
            parsing_results["auth"] = "up"
            parsing_results["username"] = args.username
            parsing_results["password"] = args.password

        #in case if the user did not insert the token or login and password !
        else :
            print("please enter the token or username and password (see help for more details !)")
            return None

        # parse the project object list : 
        project_list = None
        issues_list = None

        #if the user inserted the issues tag list 
        if args.issues : 
            issues_list = cli_parse_issues(args.issues)

        #add the same issue tag list to all the branches in all the projects inserted by the user : 
        if args.project_branch :
            project_list  = cli_parse_projects(args.project_branch)
            for project in project_list:
                if project.branches :
                    for branch in project.branches :
                        branch.issues = issues_list

        #add the poject list to the return dict 
        parsing_results["projects"] = project_list 

        #add issue tag list : to avoid looking inside each branch to find  if the user inserted the issues_list or not : 
        parsing_results["issues"] = issues_list

        #the sonarqube url : 
        parsing_results["sonarqube_url"] = args.sonarqube_url

        #the organization because we use sonarcloud for testing: 
        # we can remove it if we want to use an other version of sonar : 
        if args.organization :
            parsing_results["organization"]=args.organization
        else:
            parsing_results["organization"]="kestar"

        #if the user specified the output file name : 
        if args.output_filename:
            print("you choosed cli : ")
            parsing_results["output_filename"] = args.output_filename
        else :
            parsing_results["output_filename"] = None

        #return the dict containing the parsed project - branch-issue tag list, etc....
        return parsing_results
    #if the user did not specified the project name and the sonarqube url server : 
    else :
        
        return None
#function to parse the arg of --project-branch

def cli_parse_projects(args):

    #split the projects by , 
    projects = args.split(',')
    projects_list = []
    #for each project key 
    for parsed_project in projects :

        # parse  a single project : 
        projects_list.append(cli_parse_project(parsed_project))

    #return the project list 
    return projects_list
def cli_parse_project(project):
    #split the project key and branches name : 
    project_branches = project.split(':')

    #if the user did not insert the branch name defualt will be master : 
    branches = [Branch(name="master")]
    if len(project_branches) > 1 : 
        branches = cli_parse_branchs(project_branches[1])
        
    #create a project object and return it : 
    project_object = Project(key = project_branches[0],branches = branches)
    return project_object  
    
def cli_parse_branchs(branches):

    #split the branches : 
    splited_branches = branches.split('#')
    branches_objects = []

    #create the branches objects : 
    for splited_branch in splited_branches:
        branch = Branch(name=splited_branch)
        branches_objects.append(branch)
    return branches_objects

def cli_parse_issues(args):
    #split the issue tag list 
    issue = Issue(key=None )
    splitted_tags = args.split(',')
    issue.tags = splitted_tags
    return [issue]



