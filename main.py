import argparse
from unicodedata import name

from json_generator.parsing.parse_arguments import entry_point_cli, entry_point_file

from json_generator.models.branch import Branch

from json_generator.models.project import project



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process some integers")


    subparsers = parser.add_subparsers(help="commands",required="True" ,metavar="configuration method" ,dest="config_method")
    # for the file 
    file_parser = subparsers.add_parser('f',help="use config file ")
    file_parser.add_argument("file_path",metavar='[path of file]', help="the path of the file for example (/home/user/sonarqube.json")

    # for command line : 

    cli_parser = subparsers.add_parser('c',help="use command line")


    cli_parser.add_argument("-pb","--project-branch",metavar='',required="True" , dest="project_branch",help="insert the projects and branch of each project project_key:branch1|branch2,project... for example httpreq:master|debug,kestar:master|develop")
    cli_parser.add_argument("-u","--username",metavar='',dest="username",help="insert username")
    cli_parser.add_argument("-p","--password",metavar='',dest="password",help="insert password")
    cli_parser.add_argument("-t","--token",metavar='',dest="token",help="insert token")


    args = parser.parse_args()
    if(args.config_method=='f'):
        entry_point_file(args)
    if(args.config_method=='c'):
        entry_point_cli(args)
