

import sys
from json_generator.json_generator.generate_per_file import generate_json_for_all_files
from json_generator.json_generator.summary_information import get_summary_information
import json
from json_generator.processing.issue_processing.file_cmp import get_componentKeys
from json_generator.processing.issue_processing.issue_proc import get_unresolved_issues
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components
from json_generator.processing.project_processing.project_proc import get_issues_of_project, get_measures_of_project, get_project, get_spec_issues_of_project

# the entry function for the object : 

def main(sonar , object):
    # list of metrics keys
    metrics_keys_list = ["ncloc" , "comment_lines_density","complexity","cognitive_complexity"]
    #we need to convert the list of metrics to one string : 
    metrics_keys  = ",".join(map(str, metrics_keys_list))
    # in case the user specified the output file name else the value will be NULL
    json_file_name = None

    #file object to write the result in
    json_output_file = None

    #if the user specified the output file name 
    if object["output_filename"] :

        #create a file 
        json_file_name = object["output_filename"]+".json"

        #open the file 
        json_output_file = open(json_file_name,"w")

    #a list of json project
    json_result = []

    #handle the output details of a project 
    information_for_each_project = {}

    if json_output_file:
        
        print("the method for auth used is : "+object["auth"])
            # print all issues : 
        print("the sonar qube server is : "+object["sonarqube_url"])
        print("number of project you inserted are : "+str(len(object["projects"])))

    #run throw each project specified by the user : 
    for project in object["projects"]:
                information_for_each_project = {}
                if json_output_file:
                    print("getting information about the project : "+project.key)

                #because we tested the scripts in sonarcloud so we needed the organization name default is : kestar
                project.organization=object["organization"]

                #get the details of the project : like name visibility etc... 
                # check the parse_jsonProject method in project model in case you want to add any other field : 
                detailled_project = get_project(sonar , project)

                #if the project not exist 
                if not detailled_project:
                    if json_output_file:
                        #show an error :
                        print("Error getting informations about the project !"+project.key)
                        continue
                
                #fill the project name in the project output json : 
                information_for_each_project["project_name"] = detailled_project.name


                information_for_each_project["details"] = []
                summary_informations = None
                information_per_file = None
                branches = project.branches

                for branch in branches : 
                    # get the measures 
                    measures = get_measures_of_project(sonar , args_proj=project ,args_branch=branch , metric_keys=metrics_keys)
                    print("measures are : ")
                    print(measures)
                    project.measures = measures
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
                        if not detailled_issues:
                            continue
                        # getting the unresolved issues to calculate the summary information: 
                        if json_output_file : 
                            print("getting unresolved issues of "+project.name+" of branch : "+branch.name)
                        
                        # filter the unresolved issues 
                        unresolved_issues = get_unresolved_issues(detailled_issues)

                        # calculate the summary information about the unresolved issues 
                        summary_informations = get_summary_information(project,branch , unresolved_issues)
                        
                        # get all the files containing the issues with a specified tag list 
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch,args_issue=issue) 

                        # fill the files models with it's issues ( component of type file )
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar , issue_containing_tags=issue,measures=metrics_keys) 

                        # generate the information of each file in a json format 
                        information_per_file = generate_json_for_all_files(files_objects_with_issues)

                    else : 
                        #if the user did not specified the issues tag list git all the issues of a project: 
                        detailled_issues = get_issues_of_project(sonar=sonar , arg_proj=project, args_branch=branch)
                        #if we did not find any issue just continue to the next branch :
                        if not detailled_issues:
                            continue

                        # filter unresolved issues from all the issues list:
                        unresolved_issues = get_unresolved_issues(detailled_issues)

                        #calculate summary information of a branch based on the unresolved issues list 
                        summary_informations = get_summary_information(project,branch , unresolved_issues)  
                        
                        #get files containing issues in case of no issue tag list is specified 
                        list_files_containing_issues_only_keys= get_componentKeys(sonar=sonar,arg_proj=project,args_branch=branch) 
                        
                        # fill the files with issues related to each file  :
                        files_objects_with_issues = add_issues_to_all_components(branch=branch , components=list_files_containing_issues_only_keys , sonar=sonar , issue_containing_tags=issue,measures=metrics_keys) 
                        
                        #generate the information of each file in a json format
                        information_per_file = generate_json_for_all_files(files_objects_with_issues)
                    
                    #append the summary and information per file to the branch details section in the json file : 
                    information_for_each_project["details"].append({"summary_informations" : summary_informations , "information_per_file":information_per_file})
                
                #append the project json result to the json projects list 
                json_result.append(information_for_each_project)
    
    #if the user selected the output file name : 
    if json_output_file:
        print("generating json file......")
        json_output_file.write(str(json.dumps(json_result, indent=4))) 
        json_output_file.close()
    #if the user did not specified the output file name print the result to stdout
    else : 
        sys.stdout.write(str(json.dumps(json_result)))
              