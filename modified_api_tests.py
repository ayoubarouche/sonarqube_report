from sonarqube import SonarCloudClient

from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient

file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]
sonarclout_url = "https://sonarcloud.io/"

modified = ModifiedSonarCloudClient(sonarcloud_url = sonarclout_url,token = sonarcloud_token)

componenets = list(modified.components_issues.search_components(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc",branch="main",tags="update"))

comp = list(modified.components.search_components(organization="kestar",qualifiers = "FIL"))
print(componenets)

print("and the componenets are : ")
print("--------------------------------------")

print(comp)