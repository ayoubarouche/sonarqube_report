from ast import Num
from distutils.log import INFO
from logging import CRITICAL, critical
from re import L
from tarfile import BLOCKSIZE
from json_generator.processing.issue_processing.issue_proc import get_issues_by_category, get_issues_by_resolution, get_issues_by_severity, get_unresolved_issues


# Number of unresolved issues :

def get_numbers_of_issues_by_category(project,branch,issue):

    Numbers={}
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    codesmell_issues=get_issues_by_category(list_issues=unresolved_issues,type="CODE_SMELL")
    Bug_issues=get_issues_by_category(list_issues=unresolved_issues,type="BUG")
    print(len(Bug_issues))
    vuln_issues=get_issues_by_category(list_issues=unresolved_issues,type="VULNERABILITY")
    sec_issues=get_issues_by_category(list_issues=unresolved_issues,type="SECURITY_HOTSPOT")
    Numbers={"code_smell":len(codesmell_issues),"Bug":len(Bug_issues),"vulerability":len(vuln_issues),"security_hostpost":len(sec_issues)}
    return Numbers

def get_numbers_of_issues_by_severity(project,branch,issue):

    Numbers={}
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    major_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MAJOR")
    minor_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MINOR")
    info_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="INFO")
    blocker_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="BLOCKER")    
    critical_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="CRITICAL") 
    Numbers={"MAJOR":len(major_issues),"MINOR":len(minor_issues),"INFO":len(info_issues),"BLOCKER":len(blocker_issues),"CRITICAL":len(critical_issues)}
    return Numbers

def get_numbers_of_unres_issues(project,branch,issue):
    
    unresolved_issues=get_unresolved_issues(list_issues = issue)
    Numbers= (len(unresolved_issues))
    return Numbers

def get_summary_information(project,branch,issue=None):
    print("summary information of the project" + str(project.name)+ "and it branch"+str(branch.name))
    summ_inf={"summary_information":{"unresolved":{"total":0,
    "details":{"category":{},"severity":{}}}}}

    summ_inf["summary_information"]["unresolved"]["total"]=get_numbers_of_unres_issues(project,branch,issue)
    summ_inf["summary_information"]["unresolved"]["details"]["category"]=get_numbers_of_issues_by_category(project,branch,issue)
    summ_inf["summary_information"]["unresolved"]["details"]["severity"]=get_numbers_of_issues_by_severity(project,branch,issue)

    return summ_inf




        
        