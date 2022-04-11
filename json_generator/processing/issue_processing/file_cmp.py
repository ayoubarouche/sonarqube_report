"""
contians function to handle the component ( file)

functions : 
    * get_componentKeys : function to get all the files contians issues :
"""

from json_generator.models.component import Component
from json_generator.models.measure import Measure


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


# def get_filemetrics(sonar,arg_proj,arg_branch, metrics=[]):
#     comp =None 
#     if arg_proj:
#         if arg_branch:
#             if metrics:
#                 comp = sonar.measures.get_component_tree_with_specified_measures(component=arg_proj.key,branch=arg_branch.name,metricskeys=metrics)
#             for c in comp.keys:
#                 i=0
#                 if c == "components":
#                     for i in range(len(c)):
#                         m=[]
#                         measure_i=Measure()
#                         measure_i.parse_jsonMetric(c[i]["measures"][j])
#                         m.append(measure_i)
#                         j=j+1

def get_filemetrics(sonar,arg_proj,arg_branch, metrics):
    comp =None 
    if arg_proj:
        if arg_branch:
            if metrics:
                measures_comp =  list(sonar.measures.get_component_with_specified_measures(component=arg_proj.key, branch=arg_branch.name, metrickeys=metrics)["component"]["measures"])
                measures_list=[]
                for measures in measures_comp:
                    measure_i=Measure()
                    measure_i.parse_jsonMetric(measures)
                    measures_list.append(measure_i)
                return measures_list

        
