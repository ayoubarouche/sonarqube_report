

from json_generator.json_generator.default import generate_project
from json_generator.models.project import Project

import json
if __name__ == "__main__" :

    helloworld = Project()
    helloworld.key = "hello world"
    helloworld.name = "kestar"
    generate_project(helloworld)