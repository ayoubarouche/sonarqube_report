
import argparse
from lib2to3.pytree import convert
from unicodedata import name
from json_generator.json_generator.generate_per_file import convert_list_issues_json, generate_json_for_all_files

from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.file_cmp import get_componentKeys
from json_generator.processing.issue_processing.issue_proc import get_issues_by_resolution, get_issues_by_severity, get_unresolved_issues
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient
from json_generator.processing.project_processing.project_proc import get_branches_of_project, get_issues_of_project, get_project, get_spec_issues_of_project, parse_obj_to_json   

# the entry function for the object : 

def main(sonar , object):

    # creating the sonar app : 
     
    print("the method for auth used is : "+object["auth"])
            # print all issues : 
    print("the sonar qube server is : "+object["sonarqube_url"])
    for project in object["projects"]:
                print("the project name is : "+project.key)
                project.organization=object["organization"]
                detailled_project = get_project(sonar , project)
                print("detailled project is : "+detailled_project.lastAnalysisDate)
                for branch in project.branches : 
                    detailled_branch = get_branches_of_project(sonar, project)
                    print("the detailled branch is :"+str(detailled_branch[0].name))
                    print("the branch name is : "+branch.name)

                    if branch.issues: 
                        issue = branch.issues[0]
                        # getting the issues of branch : 
                        detailled_issues  = get_spec_issues_of_project(sonar , project , branch , issue)
                        issues_major = get_issues_by_severity(list_issues=detailled_issues,severity="MAJOR")
                        issues_wontfix = get_issues_by_resolution(list_issues = detailled_issues , resolution= "UNRESOLVED")
                        issues_unresolved = get_unresolved_issues(list_issues = detailled_issues )
                    
                        for he in issues_unresolved :
                            print("the unresolved issue is : "+str(he.tags))
                        print("the length of issues are : "+str(len(issues_major)))
                        for isss in issues_major:
                            print("the wontfix issue is : "+isss.message)
                  #      issues_with_wont_fix = get_issues_by_tag(list_issues , severity , category)
                    #    len(issues_with_wont_fix)
                        #secand part : getting issues in each file (by reverting the issues : )
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch,args_issue=issue) 
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar , issue_containing_tags=issue)
                        
                        for file in list_files_containing_issues_only_keys:
                            print("the uuid of file is : "+file.uuid)
                        print("the files are : "+str(len(files_objects_with_issues[0].issues)))
                        result = generate_json_for_all_files(files_objects_with_issues)
                        #test for the first file for now : 

                        file = files_objects_with_issues[0]

                        result_issues = convert_list_issues_json(file.issues)

                        print("the result issues for now are : ")
                        print(result_issues)
                        print("the result result is : "+str(result))
                        print("the issues are : ")
                    else : 
                        #if the user did not specified the issues tag list : 
                        detailled_issues = get_issues_of_project(sonar=sonar , projec=project, branch=branch)

                        
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
                        