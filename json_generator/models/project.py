class project :
# attributes
    def __init__(self,organization, #name of the organization 
                key=None,                #Key of the project
                name=None ,               #name of the project 
                lastAnalysisDate=None,    #date of last analyse 
                branches =[]
                ):
        self.organization = organization
        self.key = key
        self.name = name
        self.lastAnalysisDate=lastAnalysisDate
        self.branches=branches

 # Method to update the last Date
    def update_analysis_date(self,analysis_date):
        self.analysisDate = analysis_date
        return

#Method to get the branches of a project 
    def get_branches(self):
        return self.branches

   