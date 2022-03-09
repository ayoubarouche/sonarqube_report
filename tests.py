from sonarqube import SonarCloudClient

sonarclout_url = "https://sonarcloud.io/"

file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]

sonar = SonarCloudClient(sonarcloud_url=sonarclout_url , token=sonarcloud_token)


projects = list(sonar.projects.search_projects("aroucheayoubkestar"))
branches = sonar.project_branches.search_project_branches(project="linux-test")
issues = list(sonar.issues.search_issues(componentKeys="linux-test",branch="master"))
print("the list of projects is : ")
print("------------------------------------")

print(projects)

print("")
print("branches are ")
print(branches)


print()

print("the isssuer of is : ")
print(issues)