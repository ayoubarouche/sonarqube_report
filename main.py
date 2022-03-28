import argparse
from email.policy import default
from unicodedata import name
from entry import main

from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.file_cmp import get_componentKeys
from json_generator.processing.issue_processing.issue_proc import get_issues_by_severity
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient
from json_generator.processing.project_processing.project_proc import get_branches_of_project, get_project, get_spec_issues_of_project   


if __name__ == "__main__":
   

    parser = argparse.ArgumentParser(description="process some integers")


    subparsers = parser.add_subparsers(help="commands",required="True" ,metavar="configuration method" ,dest="config_method")
    # for the file 
    file_parser = subparsers.add_parser('f',help="use config file ")
    file_parser.add_argument("file_path",metavar='[path of file]', help="the path of the file for example : /home/user/sonarqube.json")

    # for command line : 

    cli_parser = subparsers.add_parser('c',help="use command line")

    cli_parser.add_argument("-s","--sonarqube-server",metavar="",required = "True", dest="sonarqube_url", help="insert the sonarqube server url ")
    cli_parser.add_argument("-pb","--project-branch",metavar='',required="True" , dest="project_branch",help="insert the projects and branch of each project project_key:branch1#branch2,project... for example httpreq:master#debug,kestar:master#develop")
    cli_parser.add_argument("-u","--username",metavar='',dest="username",help="insert username")
    cli_parser.add_argument("-p","--password",metavar='',dest="password",help="insert password")
    cli_parser.add_argument("-t","--token",metavar='',dest="token",help="insert token")
    cli_parser.add_argument("-i","--issues-tag-list",dest="issues",metavar="" , help = "insert the issue tag list")
    cli_parser.add_argument("-o","--org",dest="organization",metavar="" , help = "insert the org tag ")
    cli_parser.add_argument("-out","--output-filename",dest="output_filename",metavar="" , help = "insert the json output file name ", default=None)
    
    result = None
    args = parser.parse_args()
    if(args.config_method=='f'):
        result = entry_point_file(args.file_path)
        if not result:
            print("error parsing the json file arguments are missing !:(")
        else : 
            sonar = None
            if result["auth"] == "t":
                sonar=ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token=result["token"])
            else :
                sonar = ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token = None).auth.authenticate_user(result["username"],result["password"])
            main(object=result , sonar = sonar)
    if(args.config_method=='c'):
        #for now the command we tested is : python3 main.py c -s www.sonarqube.io -pb kestar:master#main -i bug,vur -t helloworld 
        result = entry_point_cli(args)
        if not result:
            cli_parser.print_help()
        else : 
            sonar = None
            if result["auth"] == "t":
                sonar=ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token=result["token"])
            else :
                sonar = ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token = None).auth.authenticate_user(result["username"],result["password"])
            main(object=result , sonar = sonar)