"""
contians function to handle the component ( file)

functions : 
    * get_componentKeys : function to get all the files contians issues :
"""

from json_generator.models.component import Component


def get_componentKeys(sonar,arg_proj,args_branch,args_issue=None):
    set_of_components = set()
    comp =None 
    if args_issue:
        result_issue_tags = ",".join(map(str, args_issue.tags))
        comp=list(sonar.components_issues.search_components(componentKeys=arg_proj.key,branch=args_branch.name,tags=result_issue_tags))
    else :
        comp=list(sonar.components_issues.search_components(componentKeys=arg_proj.key,branch=args_branch.name))
    if not comp:
        return None
    for i in comp:
        if i["qualifier"]=="FIL" :
            comp_object=Component(key=None)
            comp_object.parse_jsoncomponent(i)
            set_of_components.add(comp_object)

    return list(set_of_components)



