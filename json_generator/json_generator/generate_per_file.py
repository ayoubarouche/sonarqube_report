

# generating json result for each file : 


from json_generator.processing.issue_processing.issue_proc import get_issues_by_resolution, get_unresolved_issues
from json_generator.processing.project_processing.project_proc import parse_obj_to_json



def generate_json_for_all_files(files):
    result = []


    for file in files : 
        result_file = {}
        result_file["file_uuid"] = file.uuid
        result_file["file_key"] = file.key
        result_file["file_name"] = file.name
        result_file["issues"] = generate_json_for_file(file)
        result.append(result_file)
    return result

def generate_json_for_file(file):
    issues = file.issues 

    #getting unresolved issues : 
    unresolved = get_unresolved_issues(issues)
    wontfix = get_issues_by_resolution(list_issues= issues , resolution = "WONTFIX")
    #to add other type of issues  : 
    # fixed = get_issues_by_resolution(list_issues= issues , resolution = "FIXED")
    # false_positive = get_issues_by_resolution(list_issues= issues , resolution = "FALSE-POSITIVE")
    # removed = get_issues_by_resolution(list_issues= issues , resolution = "REMOVED")
    unresolved_result = []
    wontfix_result = []


    for issue in unresolved:
        unresolved_result.append(parse_obj_to_json(issue))
    for issue in wontfix:
        wontfix_result.append(parse_obj_to_json(issue))
    #to add a new type of issues : 
    # for issue in fixed:
    #     fixed_result.append(parse_obj_to_json(issue))
    # for issue in false_positive:
    #     false_positive_result.append(parse_obj_to_json(issue))
    # for issue in removed:
    #     removed_result.append(parse_obj_to_json(issue))
    result = {}

    result["unresolved"] = unresolved_result
    result["wontfix"] = wontfix_result
    #if you want to add a type of issues
    # result["fixed"] = fixed_result
    # result["false_positive"] = false_positive_result
    # result["removed"] = removed_result

    return result


def convert_list_issues_json(list_issues):
    issues_result = []

    for issue in list_issues :
        issues_result.append(parse_obj_to_json(issue))
    return issues_result