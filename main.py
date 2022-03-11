import argparse
from unicodedata import name

from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.file_cmp import get_componentKeys
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient   


if __name__ == "__main__":

    sonarclout_url = "https://sonarcloud.io/"

    file = open("access_token.txt",'r')
    line = file.readlines()
#reading the first line that contains the access token 
    sonarcloud_token = line[0]

    sonar=ModifiedSonarCloudClient(sonarcloud_url=sonarclout_url,token=sonarcloud_token)

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
    cli_parser.add_argument("-i","--issues",dest="issues",metavar="" , required="True" , help = "insert the issue tag list")

    result = None
    args = parser.parse_args()
    if(args.config_method=='f'):
        result = entry_point_file(args.file_path)
        if not result:
            print("error parsing the json file :(")
        else : 
            print("the method for auth used is : "+result["auth"])
            if result["auth"] == "t":
                print("the token is : "+result["token"])
            elif result["auth"] == "up":
                print("the username is : "+result["username"] +" and the password is : "+result["password"])

  
            print("the sonar qube url is : "+result["sonarqube-url"])
            # print all issues : 
            for project in result["projects"]:
                print("the project key is : "+project.key)
                print("-------------------------------------------")
                for branch in project.branches : 
                    print("the project branch name is : "+branch.name)
                    print()
                    for issue in branch.issues : 
                        print(" the issues are : ")
                        print(str(issue.tags))
                print()
    if(args.config_method=='c'):
        #for now the command we tested is : python3 main.py c -s www.sonarqube.io -pb kestar:master#main -i bug,vur -t helloworld 
        result = entry_point_cli(args)
        if not result:
            cli_parser.print_help()
        else : 
            print("the method for auth used is : "+result["auth"])
            # print all issues : 
            print("the sonar qube server is : "+result["sonarqube_url"])
            for project in result["projects"]:
                print("the project name is : "+project.key)
                for branch in project.branches : 
                    print("the branch name is : "+branch.name)
                    for issue in branch.issues: 
                        print("the issue is : "+str(issue.tags))
                    print()
                print()

            listr= get_componentKeys(result["projects"],result["projects"].branches,result["projects"].branches[0].issues) 

            print(listr)
            

            


    