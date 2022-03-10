import argparse
from unicodedata import name

from json_generator.parsing.parse_arguments import entry_point_cli, entry_point_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process some integers")


    subparsers = parser.add_subparsers(help="commands",required="True" ,metavar="configuration method" ,dest="config_method")
    # for the file 
    file_parser = subparsers.add_parser('f',help="use config file ")
    file_parser.add_argument("file_path",metavar='[path of file]', help="the path of the file for example (/home/user/sonarqube.json")

    # for command line : 

    cli_parser = subparsers.add_parser('c',help="use command line")


    cli_parser.add_argument("-pb","--project-branch",metavar='',required="True" , dest="project_branch",help="insert the projects and branch of each project project_key:branch1#branch2,project... for example httpreq:master#debug,kestar:master#develop")
    cli_parser.add_argument("-u","--username",metavar='',dest="username",help="insert username")
    cli_parser.add_argument("-p","--password",metavar='',dest="password",help="insert password")
    cli_parser.add_argument("-t","--token",metavar='',dest="token",help="insert token")
    cli_parser.add_argument("-i","--issues",dest="issues",metavar="" , required="True" , help = "insert the issue tag list")

    result = None
    args = parser.parse_args()
    if(args.config_method=='f'):
        entry_point_file(args)
    if(args.config_method=='c'):
        result = entry_point_cli(args)
        if not result:
            cli_parser.print_help()
        else : 
            print("the method for auth used is : "+result["auth"])
            # print all issues : 
            for project in result["projects"]:
                for branch in project.branches : 
                    for issue in branch.issues: 
                        print("the issue is : "+issue.key)
                    print()
                print()