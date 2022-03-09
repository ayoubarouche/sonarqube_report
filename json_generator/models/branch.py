# branch class :

class Branch:
    
    def __init__(self,name , # the name of the branch
                isMain=True ,# is it the main function 
                status=None, # status of the branch like (bugs , vulnerabilities , codeSmells)
                analysisDate=None, # the date of last analyse
                issues=[]):
        self.name = name
        self.isMain = isMain 
        self.status = status
        self.analysisDate = analysisDate
        self.issues=issues

    # method to update the status attribute of the branch 
    def update_status(self ,status):
        self.status = status
        return

    def update_analysis_date(self,analysis_date):
        self.analysisDate = analysis_date
        return 

    def get_issues(self):
        return self.issues