"""
contains functions to generate summary infrmation of a branch  :

"""
from json_generator.processing.issue_processing.issue_proc import get_issues_by_category, get_issues_by_severity, get_unresolved_issues
from json_generator.processing.project_processing.project_proc import parse_obj_to_json
from processing.project_processing import get_json_of_measures

# Number of unresolved issues :

def get_numbers_of_issues_by_category(issue):

    Numbers={}
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    codesmell_issues=get_issues_by_category(list_issues=unresolved_issues,type="CODE_SMELL")
    Bug_issues=get_issues_by_category(list_issues=unresolved_issues,type="BUG")
    vuln_issues=get_issues_by_category(list_issues=unresolved_issues,type="VULNERABILITY")
    sec_issues=get_issues_by_category(list_issues=unresolved_issues,type="SECURITY_HOTSPOT")
    Numbers={"code_smell":len(codesmell_issues),"Bug":len(Bug_issues),"vulerability":len(vuln_issues),"security_hostpost":len(sec_issues)}
    return Numbers

def get_numbers_of_issues_by_severity(issue):

    Numbers={}
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    major_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MAJOR")
    minor_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MINOR")
    info_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="INFO")
    blocker_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="BLOCKER")    
    critical_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="CRITICAL") 
    Numbers={"MAJOR":len(major_issues),"MINOR":len(minor_issues),"INFO":len(info_issues),"BLOCKER":len(blocker_issues),"CRITICAL":len(critical_issues)}
    return Numbers

def get_numbers_of_unres_issues(issue):
    
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    Numbers= (len(unresolved_issues))
    return Numbers




def get_summary_information(project,branch,issue=None):
    summ_inf= {"summary_information":{"branch-name":branch.name,"date-Last-Analysis":project.lastAnalysisDate,
    "unresolved-issues":{"total":0,"issues-details":{"category":{},"severity":{}}}}}
    summ_inf["summary_information"]["measures"] = get_json_of_measures(project.measures)
    summ_inf["summary_information"]["unresolved-issues"]["total"]=get_numbers_of_unres_issues(issue)
    summ_inf["summary_information"]["unresolved-issues"]["issues-details"]["category"]=get_numbers_of_issues_by_category(issue)
    summ_inf["summary_information"]["unresolved-issues"]["issues-details"]["severity"]=get_numbers_of_issues_by_severity(issue)

    return summ_inf["summary_information"]






        
        