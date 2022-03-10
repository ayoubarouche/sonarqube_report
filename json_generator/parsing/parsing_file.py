
import json 
def parse_file(file):
    with open(file) as json_file :
        json_object = json.load(json_file)
        json_file.close()
    project = json_object['project']

    username = json_object['username']