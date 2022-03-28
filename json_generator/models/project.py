

from json_generator.models.branch import Branch


class Project :
# attributes
    def __init__(self,organization=None, #name of the organization 
                key=None,                #Key of the project
                name=None ,               #name of the project 
                lastAnalysisDate=None,    #date of last analyse 
                branches =[Branch(name="master")]
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

#Method to parse from Json to object
    def parse_jsonProject(self,json_str):
        self.organization=json_str['organization']
        self.key=json_str['key']
        self.name=json_str['name']
        self.qualifier=json_str['qualifier']
        self.visibility=json_str['visibility']
        self.lastAnalysisDate=json_str['lastAnalysisDate']
        self.revision=json_str['revision']
        return self



