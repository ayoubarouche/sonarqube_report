"""
a model to handle an issue it will generate informations like the component infos (componenet contains the file name etc) .
"""


class Issue:

    def __init__(self,
                 key, #the key of the issue
                 rule=None, #the rule of the issue example : MagicNumberCheck
                 status=None, # the status of the issue : resolved
                 resolution=None, # resolution : false-positive
                 severity=None, # Minor - Major
                 message=None, # the message of the issue
                 author=None,  # the author of the issue 
                 components=[], # the components that had the issue
                 tags=[],
                 comments = []
                 ) : # tags of the componenet
        self.key = key 
        self.rule = rule 
        self.status = status 
        self.resolution = resolution 
        self.severity = severity 
        self.message = message 
        self.author = author 
        self.components = components 
        self.tags = tags
        self.comments = comments
        return
    def get_status(self):
        return self.status 


class Component :
    def __init__(self , 
                    key , # the key of the component 
                    enabled=None, # is it enabled or not 
                    qualifier=None, # the type example FIL ( file )
                    name=None, # the name of the component 
                    path=None, # the path of the component 
                ):
        self.key = key 
        self.enabled = enabled 
        self.qualifeir = qualifier
        self.name = name 
        self.path = path
        return
    #getting the component name : (imporatant for the issue : )\

    def get_component_name(self):
        return self.name
    def get_component_path(self):
        return self.path



# to handle the convertion from the issue -> files (components) to file(component) -> issues
class FileMapping: 
    def __init__(self,issue_key , component_key) :
        self.issue_key = issue_key 
        self.component_key = component_key

    def get_component_key(self):
        return self.component_key 
    
    def get_issue_key(self):
        return self.issue_key

        