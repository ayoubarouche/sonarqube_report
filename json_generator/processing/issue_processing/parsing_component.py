



from json_generator.models.issue import Component, Issue


def add_issues_to_component(sonar , component,issue_tags,branch):
    result_issue_tags = ",".join(map(str, issue_tags))
    print("the list of tags inside add issues is : "+result_issue_tags)
    if issue_tags:
        issues = list(sonar.issues.search_issues(fileUuids=component.uuid,tags=result_issue_tags,branch=branch.name))
    else : 
        issues = list(sonar.issues.search_issues(fileUuids=component.uuid,branch=branch.name))

    if not issues :
        print("there is no issues for the component : "+str(component.key)+" and for tags : "+str(issue_tags) +" and branch : "+branch.name)
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


def add_issues_to_all_components(sonar , components ,issue_containing_tags ,  branch):

    result_components = []

    for component in components:
        
        issues = add_issues_to_component(sonar = sonar , component = component ,issue_tags=issue_containing_tags.tags , branch = branch)
        if issues : 
            print("there is issues ")
            comp = Component(key=component.key ,name = component.name ,  issues = issues)
            result_components.append(comp)
        else : 
            print("there is no issues !")
    return result_components