# sonarqube_report
## python script to generate reports in python from the SonarQube server
---
## HOW TO USE THE SCRIPT:

### install the sonarqube library : 

##### pip install sonarqube
---
### generel overview

##### Use Case diagram :
the Main Functionalities of the project is :

<img src="doc/diagrams/Use_Case_diagram/diag_use_case.PNG">

##### Sequence diagram : 

the general idea of how the script works is : 

<img src="doc/diagrams/sequence_diagram/requesting_json_format_sequence_diagram.jpg">

The sequence diagram of Data processing part is : 

<img src="doc/diagrams/sequence_diagram/Data_processing_sequence_diagram.jpg">

### general architecture 
The project has 4 main folders 

##### Models :
this folder contains 3 python files , each file has a function to parse from the json string to a model:
* Project.py: contains Project class which has attributes that the api return
* branch.py:  contains Project Branch which has attributes that the api return
* issue.py:  contains Issue and Component class which each class has attributes that the api return 

##### Parsing :
this folder is to parse the command ligne and the config file:
1. parse_arguments.py: this file contains functions to parse the command line 
   - cli_parse_projects(args): this method parse the project part in cli and return the list of project mentionned in it
        - output : list of project 
   - cli_parse_project(): it splits the branches from the project 
        - output : list of branch object 
   - cli_parse_branchs(): split between the branches mentionned 
        - output: list of banches of a project
   - cli_parse_issues(): split between issues 
        - output: list of issues of a branch 
   - cli_entry_point() : it parse the whole command ligne, verify if all the parameters required are present and the authentication method
2. parsing_file.py: it contains methods to parse the config file , same functionalities of the first file functions

##### Processing 
1. Modified_api: we got inspired by the sonarcoud classes to create a modifiedsonarcloudcliend class that inherit from the sonarcloudclient class to resolve the                      problem of getting the issues of a file .
    - Component.py: contains two classes modifiedsonarcloudclient and modifiedsonarcloudIssues which has the search_component() function that returns the components                     containing the issues given as argument
2. Issue_processing : 
    - File_cmp.py : has a function to get a list of components thats contains the files where the issues given are mentionned.
    - parsing_component.py: has functions to search a list of issues by giving a component key
    - issue_proc.py:  funtions to get issues by category,severity and resolution
    
3. Project_proc.py : tofr scrape data from the api

##### json_generator:
    - summary_generator : functions tv get summary informations as dictionaty
    - generate_per_file: functions to get the information of file as a ditionary 
    
##### Pdf__generator:
    -Body.py: functions that parse from json to pdf using FPDF Library
    
##### Excel_generator:
    - generatetoexcel.py: functions that parse from json to excel using xlswritter Library
   
