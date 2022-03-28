"""
a model to handle an issue if you want to add any other field in the generated json file please add it to the parse_jsonissues and in the constructor
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
                 type=None,
                 creationDate=None,
                 updateDate=None,
                 components=[], # the components that had the issue
                 tags=[],
                 comments = None,
                 line = None
                 ) : # tags of the componenet
        self.key = key 
        self.rule = rule 
        self.status = status 
        self.resolution = resolution 
        self.severity = severity 
        self.message = message 
        self.author = author 
        self.type=type
        self.creationDate=creationDate
        self.updateDate=updateDate
        self.components = components 
        self.tags = tags
        self.comments = comments
        self.line = line
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
        if 'type' in json_str:
            self.type=json_str['type']
        if 'creationDate' in json_str:
            self.creationDate=json_str['creationDate']
        if 'updateDate' in json_str:
            self.updateDate=json_str['updateDate']
        if 'components' in json_str:
            self.components=json_str['components']
        if 'tags' in json_str:
            self.tags=json_str['tags']
        if 'comments' in json_str:
            self.comments= json_str['comments']
        if 'line' in json_str:
            self.line = json_str['line']
