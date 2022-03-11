from json_generator.models.issue import Component
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient   
from json_generator.parsing.parse_arguments import cli_parse_projects, cli_parse_branchs,cli_parse_issues,cli_parse_project
import json 

# sonarclout_url = "https://sonarcloud.io/"

# file = open("access_token.txt",'r')
# line = file.readlines()
# #reading the first line that contains the access token 
# sonarcloud_token = line[0]

# sonar=ModifiedSonarCloudClient(sonarcloud_url=sonarclout_url,token=sonarcloud_token)

# arg_proj = cli_parse_project(arg1)
# args_branch=cli_parse_branchs(arg3)
# args_issue=cli_parse_issues(arg4)


def get_componentKeys(arg_proj,args_branch,args_issue):
    comp=list(sonar.components_issues.search_components(componentKeys=arg_proj.key,branch=args_branch.name,tags=args_issue.tags))
    l=len(comp)
    listofcomponent=[]
    
    for i in comp:
        if i["qualifier"]=="FIL":
            listofcomponent.append(comp[i)
        
    return listofcomponent


