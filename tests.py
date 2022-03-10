from sonarqube import SonarCloudClient

sonarclout_url = "https://sonarcloud.io/"

file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]

sonar = SonarCloudClient(sonarcloud_url=sonarclout_url , token=sonarcloud_token)


projects = list(sonar.projects.search_projects("kestar"))
branches = sonar.project_branches.search_project_branches(project="ayoubarouche_linux-autotools-gh-actions-sc")
issues = list(sonar.issues.search_issues(componentKeys="ayoubarouche_linux-autotools-gh-actions-sc",branch="main"))
component = sonar.components.get_project_component_and_ancestors("ayoubarouche_linux-autotools-gh-actions-sc")
print("the list of projects is : ")
print("------------------------------------")

print(projects)

print("")
print("branches are ")
print(branches)
print(type(branches))


print()

print("the isssuer of is : ")
print(issues[0])

print()
print("cmponent is :")
print(component)