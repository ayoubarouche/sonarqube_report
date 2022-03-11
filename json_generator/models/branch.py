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


#Testing 
jsn= {'name': 'master', 'isMain': True, 'type': 'LONG', 'status': {'bugs': 0, 'vulnerabilities': 0, 'codeSmells': 0}, 
'analysisDate': '2022-03-07T14:09:21+0100', 'commit': {'sha': 'fc24e4e8c8f76b2de52c8edf3ff5ef5db855b610'}}

br = Branch()
br.parse_jsonbranch(jsn)
print(br.name,br.status)