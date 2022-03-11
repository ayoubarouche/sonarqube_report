



from json_generator.models.issue import Component, Issue


def add_issues_to_component(sonar , component,tags,branch):
    issues = list(sonar.issues.search_issues(componentKeys=component.key,tags=tags,branch=branch))
    if not issues :
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


def add_issues_to_all_components(sonar , components ,tags ,  branch):

    result_components = []

    for component in components:
        issues = add_issues_to_component(sonar = sonar , component = component ,tags=tags , branch = branch)
        if issues : 
            comp = Component(key=component.key , issues = issues)
            result_components.append(comp)
    return result_components