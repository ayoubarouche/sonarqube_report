from sonarqube import SonarCloudClient

sonarclout_url = "https://sonarcloud.io/"

file = open("access_token.txt",'r')
line = file.readlines()
#reading the first line that contains the access token 
sonarcloud_token = line[0]

sonar = SonarCloudClient(sonarcloud_url=sonarclout_url , token=sonarcloud_token)


projects = list(sonar.projects.search_projects("aroucheayoubkestar"))

print("the list of projects is : ")
print("------------------------------------")

print(projects)