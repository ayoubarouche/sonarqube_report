# branch class :

class Branch:
    
    def __init__(self,name=None , # the name of the branch
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
    
    #Method to parse from Json to object
    def parse_jsonbranch(self,json_str):
        self.name=json_str['name']
        self.isMain=json_str['isMain']
        self.type=json_str['type']
        self.status=json_str['status']
        self.analysisDate=json_str['analysisDate']
        self.commit=json_str['commit']
        return self

