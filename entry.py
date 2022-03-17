
from lib2to3.pytree import convert
import sys
from unicodedata import name
from json_generator.json_generator.generate_per_file import convert_list_issues_json, generate_json_for_all_files
from json_generator.json_generator.summary_information import get_summary_information
import json
from json_generator.parsing.parse_arguments import entry_point_cli
from json_generator.parsing.parsing_file import entry_point_file
from json_generator.processing.file_cmp import get_componentKeys
from json_generator.processing.issue_processing.issue_proc import get_issues_by_resolution, get_issues_by_severity, get_unresolved_issues
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient
from json_generator.processing.project_processing.project_proc import get_branches_of_project, get_issues_of_project, get_project, get_spec_issues_of_project, parse_obj_to_json   

# the entry function for the object : 

def main(sonar , object):
    json_file_name = None
    json_output_file = None
    # creating the sonar app : 
    if object["output_filename"] :
        json_file_name = object["output_filename"]+".json"
        json_output_file = open(json_file_name,"w")
    json_result = []
    information_for_each_project = {}
    if json_output_file:
        
        print("the method for auth used is : "+object["auth"])
            # print all issues : 
        print("the sonar qube server is : "+object["sonarqube_url"])
        print("number of project you inserted are : "+str(len(object["projects"])))
    for project in object["projects"]:
                information_for_each_project = {}
                if json_output_file:
                    print("getting information about the project : "+project.key)
                project.organization=object["organization"]
                detailled_project = get_project(sonar , project)
                if not detailled_project:
                    if json_output_file:
                        print("Error getting informations about the project !"+project.key)
                    return 
                information_for_each_project["project_name"] = detailled_project.name
                information_for_each_project["details"] = []
                summary_informations = None
                information_per_file = None
                branches = project.branches
                # if the user specified the branches : 
                if not branches :
                    branches = get_branches_of_project(sonar, project)

                for branch in branches : 
                    # for handling the issues that user had inserted :
                    #if the user inserted the issue by file for each branch :
                    issue = None 
                    if branch.issues :
                        issue = branch.issues[0]
                    #if the user did not insert the issue in config file and object["issues"] 
                    if not issue and object["issues"]:
                        issue = object["issues"][0]
                    if issue: 
                        # getting the details of a branch (like issues number and so on )
                        detailled_issues  = get_spec_issues_of_project(sonar , project , branch , issue)
                        # getting the unresolved issues : 
                        unresolved_issues = get_unresolved_issues(detailled_issues)
                        summary_informations = get_summary_information(project,branch , unresolved_issues)
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch,args_issue=issue) 
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar , issue_containing_tags=issue) 
                        information_per_file = generate_json_for_all_files(files_objects_with_issues)

                    else : 
                        #if the user did not specified the issues tag list : 
                        detailled_issues = get_issues_of_project(sonar=sonar , arg_proj=project, args_branch=branch)
                        unresolved_issues = get_unresolved_issues(detailled_issues)
                        summary_informations = get_summary_information(project,branch , unresolved_issues)  
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch) 
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar)
                        information_per_file = generate_json_for_all_files(files_objects_with_issues)

                    information_for_each_project["details"].append({"summary_informations" : summary_informations , "information_per_file":information_per_file})
                json_result.append(information_for_each_project)
    
    
    if json_output_file:
        print("generating json file......")
        json_output_file.write(str(json.dumps(json_result, indent=4))) 
        json_output_file.close()
    else : 
        sys.stdout.write(str(json.dumps(json_result)))
              