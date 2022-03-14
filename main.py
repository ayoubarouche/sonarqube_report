import argparse
from unicodedata import name

from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.file_cmp import get_componentKeys
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient
from json_generator.processing.project_processing.project_proc import get_spec_issues_of_project   


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
    cli_parser.add_argument("-o","--org",dest="organization",metavar="" , help = "insert the org tag ")

    result = None
    args = parser.parse_args()
    if(args.config_method=='f'):
        result = entry_point_file(args.file_path)
        if not result:
            print("error parsing the json file :(")
        else : 
            print("the method for auth used is : "+result["auth"])
            # print all issues : 
            print("the sonar qube server is : "+result["sonarqube_url"])
            for project in result["projects"]:
                print("the project name is : "+project.key)
                project.organization=result["organization"]
                for branch in project.branches : 
                    print("the branch name is : "+branch.name)

                    if branch.issues: 
                        issue = branch.issues[0]
                        # getting the issues of branch : 
                        detailled_issues  = get_spec_issues_of_project(sonar , project , branch , issue)
                  #      issues_with_wont_fix = get_issues_by_tag(list_issues , severity , category)
                    #    len(issues_with_wont_fix)
                        #secand part : getting issues in each file 
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch,args_issue=issue) 
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar , issue_containing_tags=issue)

                        print("the issues are : ")
                    else : 

                        # for iss in issues:
                        #     print("the issue message is : "+iss.message)
                        # print("the issue is : "+str(issue.tags))
                        
                        # print("the list is : ")
                        # print(str(len(listr)))
                        # print("the length is " +str(len(listr)))
                        
                        # print("the issue containing tags is :"+str(issue.tags))
                        # for compo in componenets :
                        #     print('for the component : '+compo.key)
                        #     for hello in compo.issues : 
                        #         print("the issue is : "+str(hello.key)+" and the resolution is : "+str(hello.creationDate))
                
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
                project.organization=result["organization"]
                for branch in project.branches : 
                    print("the branch name is : "+branch.name)
                    for issue in branch.issues: 
                        print("the issue is : "+str(issue.tags))
                        listr= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch,args_issue=issue) 
                        print("the list is : ")
                        print(str(len(listr)))
                        print("the length is " +str(len(listr)))
                        componenets = add_issues_to_all_components(branch=branch , components=listr , sonar=sonar , issue_containing_tags=issue)
                        print("the issue containing tags is :"+str(issue.tags))
                        for compo in componenets :
                            print('for the component : '+compo.key)
                            for hello in compo.issues : 
                                print("the issue is : "+str(hello.key)+" and the resolution is : "+str(hello.severity))
                print()
                print()


           
            

            


    