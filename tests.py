from json_generator.models.issue import Component
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient   

sonarclout_url = "https://sonarcloud.io/"

file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]

sonar=ModifiedSonarCloudClient(sonarcloud_url=sonarclout_url,token=sonarcloud_token)

Mdf=list(sonar.components_issues.search_components(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc:src/main.cpp",branch="main",tags="security,update"))

projects = list(sonar.projects.search_projects("kestar"))
branches = sonar.project_branches.search_project_branches(project="ayoubarouche_linux-autotools-gh-actions-sc")
issues = list(sonar.issues.search_issues(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc:src/main.cpp",branch="main"))
# components = sonar.components.get_project_component_and_ancestors("ayoubarouche_linux-autotools-gh-actions-sc",branch="main")
#cmp=Component(key=None).search_components_in_issues(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc",branch="main")
# sonar.issues.issue_set_tags("AX9vlR8A1T4myP5e-Jjo","security")
# components = list(sonar.components.search_components(organization ="kestar",qualifiers="FIL"))
# components = list(sonar.components.get_components_tree(component="ayoubarouche_linux-autotools-gh-actions-sc", qualifiers="FIL"))



# print()
# print("the list of projects is : ")
# print("------------------------------------")


# print(projects)
# # print(type(projects))

# print("")
# print("branches are ")
# print(branches)
# print(type(branches))
# print(type(branches["branches"][0]["name"]))


# print()

# print("the isssuer of is : ")
print(issues)
# print(len(issues))
# print(type(issues))

# print()
# print("cmponent is :")

# print(Mdf)
# print(components)
