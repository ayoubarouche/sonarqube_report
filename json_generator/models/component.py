

"""
a model to handle the file component if you want to add any other field you can do that by changing the parse_jsoncomponent
"""
class Component :
    def __init__(self , 
                    key , # the key of the component 
                    enabled=None, # is it enabled or not 
                    qualifier=None, # the type example FIL ( file )
                    name=None, # the name of the component 
                    path=None,
                    uuid=None,
                    issues = [],
                    measures = None # the path of the component 
                ):
        self.key = key 
        self.enabled = enabled 
        self.qualifeir = qualifier
        self.name = name 
        self.path = path
        self.issues = issues
        self.uuid=uuid
        self.measures = measures
        
    #getting the component name : (imporatant for the issue : )\

    def get_component_name(self):
        return self.name
    def get_component_path(self):
        return self.path

    #parse json from the API
    def parse_jsoncomponent(self,json_str):

        if 'key' in json_str:
            self.key=json_str['key']
        if 'enabled' in json_str:
            self.enabled=json_str['enabled']
        if 'qualifier' in json_str:    
            self.qualifier=json_str['qualifier']
        if 'name' in json_str:
            self.name=json_str['name']
        if 'uuid' in json_str:
            self.uuid=json_str['uuid']
        if 'path' in json_str:
            self.path=json_str['path']
        
    #parse json from the big json file 
    def parse_jsoncomponent_from_output_file(self, json_str):
        
        if 'file_uuid' in json_str :
            self.uuid = json_str["file_uuid"]
        if 'file_key' in json_str :
            self.key = json_str["file_key"]
        if 'file_name' in json_str :
            self.name = json_str["file_name"]
        if 'measures' in json_str:
            self.measures=json_str["measures"]

        print("________________________________________________________________")
        print (self.measures)
    
    def __hash__(self):
        return hash((self.key, self.uuid, self.name))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.key == other.key 
 

