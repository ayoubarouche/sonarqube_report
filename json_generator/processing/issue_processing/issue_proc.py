
#processing the issues and return any type of isssue we want : 

#getting issues with specific severity :

def get_issues_by_severity(list_issues, severity):
    result = [issue for issue in list_issues if issue.severity == severity]
    return result

#getting issues with specific category : 

def get_issues_by_category(list_issue,type):
   result=[issue for issue in list_issue if issue.type != type]
   return result