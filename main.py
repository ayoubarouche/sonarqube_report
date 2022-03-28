import argparse
from entry import main

from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.modified_api.modified_sonar_api import ModifiedSonarCloudClient


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

    #if the user want to use the config file method : 
    if(args.config_method=='f'):

        #parse the config file : 
        result = entry_point_file(args.file_path)

        #if parsing generate error : 
        if not result:
            print("error parsing the json file arguments are missing !:(")
        else : 

            #create the sonarqube connection : 
            sonar = None
            if result["auth"] == "t":
                #in our case we used the sonarcloud solution : 
                #if you want to use any other sonar type like sonarcommunity please visit the ModifiedSonarCloudClient class 
                #and change the class that he inheret  : 
                
                #in case the user used token method : 
                sonar=ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token=result["token"])
            else :

                #if the user want to use the login and password method
                # this method not working for sonarcloud  :
                sonar = ModifiedSonarCloudClient(sonarcloud_url=result["sonarqube_url"],token = None).auth.authenticate_user(result["username"],result["password"])
            
            #the main function : 
            main(object=result , sonar = sonar)
    if(args.config_method=='c'):
        #if the user want to use cli method : 
        #for now the command we tested is : python3 main.py c -s www.sonarqube.io -pb kestar:master#main -i bug,vur -t helloworld 
        
        #parse the command line args : 
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