"""
contians functions to manipulate the issues processing : like filtring etc...

functions : 
    * get_issues_by_severity : function to filter only issues with a specified severity.
    * get_issues_by_category : function to filter issues based on thier category
    * get_issues_by_resolution : functon to filter issues based on thier resolution
    * get_unresolved_issues : function to filter issues that they are not resolved yet.
"""
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

    #filtering  based on the status and the resolution : 
    result=[issue for issue in list_issues if issue.status == 'OPEN' or not issue.resolution]
    return result
