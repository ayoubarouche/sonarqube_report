import json
from collections import namedtuple
from json import JSONEncoder

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

#Assume you received this JSON response
studentJsonData = " {'organization': 'aroucheayoubkestar',\
 'key': 'linux-test', \
'name': 'linux-test', \
 'qualifier': 'TRK', 'visibility': 'public', 'lastAnalysisDate': '2022-03-07T14:09:21+0100', \
'revision': 'fc24e4e8c8f76b2de52c8edf3ff5ef5db855b610'}"

# Parse JSON into an object with attributes corresponding to dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(student.name, student.key)