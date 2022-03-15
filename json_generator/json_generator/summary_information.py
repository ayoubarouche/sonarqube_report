from ast import Num
from distutils.log import INFO
from logging import CRITICAL, critical
from re import L
from tarfile import BLOCKSIZE
from json_generator.processing.issue_processing.issue_proc import get_issues_by_category, get_issues_by_resolution, get_issues_by_severity


# Number of unresolved issues :

def get_numbers_of_issues_by_category(project,branch,issue):

    Numbers={}
    unresolved_issues=get_issues_by_resolution(list_issues = issue , resolution= "UNRESOLVED")
    codesmell_issues=get_issues_by_category(list_issues=unresolved_issues,type="CODE_SMELL")
    Bug_issues=get_issues_by_category(list_issues=unresolved_issues,type="BUG")
    print(len(Bug_issues))
    vuln_issues=get_issues_by_category(list_issues=unresolved_issues,type="VULNERABILITY")
    sec_issues=get_issues_by_category(list_issues=unresolved_issues,type="SECURITY_HOTSPOT")
    Numbers={"code_smell":len(codesmell_issues),"Bug":len(Bug_issues),"vulerability":len(vuln_issues),"security_hostpost":len(sec_issues)}
    return Numbers

def get_numbers_of_issues_by_severity(project,branch,issue):

    Numbers={}
    unresolved_issues=get_issues_by_resolution(list_issues = issue , resolution= "UNRESOLVED")
    major_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MAJOR")
    minor_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="MINOR")
    info_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="INFO")
    blocker_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="BLOCKER")    
    critical_issues=get_issues_by_severity(list_issues=unresolved_issues,severity="CRITICAL") 
    Numbers={"MAJOR":len(major_issues),"MINOR":len(minor_issues),"INFO":len(info_issues),"BLOCKER":len(blocker_issues),"CRITICAL":len(critical_issues)}

    return Numbers

def get_numbers_of_unres_issues(project,branch,issue):

    Numbers={}
    unresolved_issues=get_issues_by_resolution(list_issues = issue , resolution= "UNRESOLVED")
    Numbers={"Unresolved": len(unresolved_issues)}
    return Numbers

    

        
        