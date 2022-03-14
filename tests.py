from json_generator.models.issue import Component
from json_generator.processing.modified_api.Component import ModifiedSonarCloudClient   
<<<<<<< HEAD
from json_generator.processing.issue_processing.parsing_component import add_issues_to_all_components   
=======
from json_generator.processing.file_cmp import get_componentKeys
>>>>>>> a62e09b82288882dd8fb7d8f8e1fb05caaaa8ca9

sonarclout_url = "https://sonarcloud.io/"
file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]

sonar=ModifiedSonarCloudClient(sonarcloud_url=sonarclout_url,token=sonarcloud_token)

Mdf=list(sonar.components_issues.search_components(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc",branch="main",tags="security,update"))

projects = list(sonar.projects.search_projects("kestar"))
branches = sonar.project_branches.search_project_branches(project="ayoubarouche_linux-autotools-gh-actions-sc")
issues = list(sonar.issues.search_issues(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc:src/main.cpp",branch="main",tags="update,change"))
# components = sonar.components.get_project_component_and_ancestors("ayoubarouche_linux-autotools-gh-actions-sc",branch="main")
#cmp=Component(key=None).search_components_in_issues(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc",branch="main")
# sonar.issues.issue_set_tags("AX9vlR8A1T4myP5e-Jjo","security")
<<<<<<< HEAD
component = list(sonar.components.search_components(organization ="kestar",qualifiers="FIL"))
components = list(sonar.components.get_components_tree(component="ayoubarouche_linux-autotools-gh-actions-sc", qualifiers="FIL"))
componts = []
comp1 = Component(key="ayoubarouche_linux-autotools-gh-actions-sc:src/hello.cpp")
comp2 = Component(key="ayoubarouche_linux-autotools-gh-actions-sc:src/main.cpp")
componts.append(comp1)
componts.append(comp2)
branch="main"
comps = add_issues_to_all_components(sonar=sonar , components = componts , branch=branch,tags="update")
=======
# components = list(sonar.components.search_components(organization ="kestar",qualifiers="FIL"))
# components = list(sonar.components.get_components_tree(component="ayoubarouche_linux-autotools-gh-actions-sc", qualifiers="FIL"))
cmp=get_componentKeys("ayoubarouche_linux-autotools-gh-actions-sc","main","security")

>>>>>>> a62e09b82288882dd8fb7d8f8e1fb05caaaa8ca9

# print()
print("the list of projects is : ")
print("------------------------------------")


# print(projects)
# print(type(projects))

# print("")
# print("branches are ")
# print(branches)
# print(type(branches))
# print(type(branches["branches"][0]["name"]))


# print()

# print("the isssuer of is : ")
<<<<<<< HEAD
# print(issues)
# # print(type(issues))
=======
#print(issues)
# print(len(issues))
# print(type(issues))
>>>>>>> a62e09b82288882dd8fb7d8f8e1fb05caaaa8ca9

# print()
# print("cmponent is :")
# print(issues)

# print(branches["branches"][0])
print(type(Mdf))
# print(issues)
# print(type(issues))
# print(len(issues))
# print(issues[0]["tags"])
print(component)
print(type(Mdf))
