"""
a model to handle an issue it will generate informations like the component infos (componenet contains the file name etc) .
"""

from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_ISSUES_SEARCH_ENDPOINT,
    API_ISSUES_ASSIGN_ENDPOINT,
    API_ISSUES_DO_TRANSITION_ENDPOINT,
    API_ISSUES_ADD_COMMENT_ENDPOINT,
    API_ISSUES_EDIT_COMMENT_ENDPOINT,
    API_ISSUES_DELETE_COMMENT_ENDPOINT,
    API_ISSUES_SET_SEVERITY_ENDPOINT,
    API_ISSUES_SET_TYPE_ENDPOINT,
    API_ISSUES_AUTHORS_ENDPOINT,
    API_ISSUES_BULK_CHANGE_ENDPOINT,
    API_ISSUES_CHANGELOG_ENDPOINT,
    API_ISSUES_SET_TAGS_ENDPOINT,
    API_ISSUES_TAGS_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGE_GET

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
    
    def parse_jsonissues(self,json_str):
        if 'key' in json_str:
            self.key= json_str['key'] 
        if 'rule' in json_str: 
            self.rule=json_str['rule']
        if 'resolution' in json_str:
            self.resolution=json_str['resolution']
        if 'status' in json_str:
            self.status=json_str['status']
        if 'severity' in json_str:    
            self.severity=json_str['severity']
        if 'message' in json_str:
            self.message=json_str['message']
        if 'author' in json_str:
            self.author=json_str['author']
        if 'components' in json_str:
            self.components=json_str['components']
        if 'tags' in json_str:
            self.tags=json_str['tags']
        if 'comments' in json_str:
            self.comments=json_str['comments']



class Component :
    def __init__(self , 
                    key , # the key of the component 
                    enabled=None, # is it enabled or not 
                    qualifier=None, # the type example FIL ( file )
                    name=None, # the name of the component 
                    path=None,
                    issues = [] # the path of the component 
                ):
        self.key = key 
        self.enabled = enabled 
        self.qualifeir = qualifier
        self.name = name 
        self.path = path
        self.issues = issues
        return
        
    #getting the component name : (imporatant for the issue : )\

    def get_component_name(self):
        return self.name
    def get_component_path(self):
        return self.path

    def parse_jsoncomponent(self,json_str):
        if 'key' in json_str:
            self.key=json_str['key']
        if 'enabled' in json_str:
            self.enabled=json_str['enabled']
        if 'qualifier' in json_str:    
            self.qualifier=json_str['qualifier']
        if 'name' in json_str:
            self.name=json_str['name']
        if 'path' in json_str:
            self.path=json_str['path']

