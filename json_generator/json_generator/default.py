#testing the generator : 
import json 
def generate_project(project):
    print(json.dumps(project.__dict__))

