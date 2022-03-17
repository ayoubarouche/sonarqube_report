



import json
from json_generator.models.issue import Component, Issue


def add_issues_to_component(sonar , component,branch , issue_tags=None):
    
    if issue_tags:
        result_issue_tags = ",".join(map(str, issue_tags))
        issues = list(sonar.issues.search_issues(componentKeys=component.key,tags=result_issue_tags,branch=branch.name))
    else : 
        issues = list(sonar.issues.search_issues(componentKeys=component.key,branch=branch.name))

    if not issues :
        print("there is no issues for the component : "+str(component.uuid)+" and for tags : "+str(issue_tags) +" and branch : "+branch.name)
        return None
    issues_objects = []
    for issue in issues:
        print("the issue is : ")
        print("--------------------")
        print(issue)
        issue_object = Issue(key=None)
        issue_object.parse_jsonissues(issue)
        print("the issue key is : ")
        print("--------------------------")
        print(issue_object.key)
        issues_objects.append(issue_object)
    return issues_objects


def add_issues_to_all_components(sonar , components ,branch , issue_containing_tags=None ):

    result_components = []

    for component in components:
        if issue_containing_tags: 
            issues = add_issues_to_component(sonar = sonar , component = component ,issue_tags=issue_containing_tags.tags , branch = branch)
        else :
               issues = add_issues_to_component(sonar = sonar , component = component ,issue_tags=None , branch = branch)
         
        if issues : 
            print("there is issues ")
            comp = Component(key=component.key ,name = component.name ,  issues = issues, uuid = component.uuid)
            result_components.append(comp)
        else : 
            print("there is no issues !")
    return result_components

def parse_list_json_issues_to_list_json_objects(json_issues_list):
    issues_objects = []
    for json_issue in json_issues_list:
        issue_object = Issue(key=None)
        issue_object.parse_jsonissues(json_str=json.loads(json_issue))
        issues_objects.append(issue_object)
    return issues_objects