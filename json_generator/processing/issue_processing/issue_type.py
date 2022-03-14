def get_issues_by_category(list_issue,type):
   result=[issue for issue in list_issue if issue.type != type]
   return result