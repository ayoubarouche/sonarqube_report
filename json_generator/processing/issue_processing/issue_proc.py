
#processing the issues and return any type of isssue we want : 

#getting issues with specific severity :

def get_issues_by_severity(list_issues, severity):
    result = [issue for issue in list_issues if issue.severity == severity]
    return result

#getting issues with specific category : 

def get_issues_by_category(list_issues,type):
   result=[issue for issue in list_issues if issue.type == type]
   return result


#getting the issues with specific resolution :

def get_issues_by_resolution(list_issues , resolution):
    result=[issue for issue in list_issues if issue.resolution == resolution]
    return result

#get unresolved issues : 

def get_unresolved_issues(list_issues ):
    result=[issue for issue in list_issues if issue.status != "RESOLVED"]
    return result
