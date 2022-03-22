import argparse
import json
from operator import index
from unicodedata import category
import pandas as pd 
from csvgenerator.generatetoexcelcopy import ExcelFormatter
import xlsxwriter

parser = argparse.ArgumentParser(description="process some integers")

parser.add_argument("-f","--file",metavar="", required=False , dest="file", help="insert the sonarqube server url ")

args = parser.parse_args()
json_file = None
data = None
if args.file :
    
    json_file = open(args.file,'r')
    data = json.load(json_file)
else: 
    try:
        json_file = sys.stdin.readline()
        data = json.loads(str(json_file))
    except:
        print(str(json_file))
        print("error in the command !")
        exit()

files = data[0]["details"][1]["information_per_file"]
branches=data[0]["details"][0]["summary_informations"]
        # access to each file :
        # 
        # #creating the sheet for each branch : 
        #
       

excel = ExcelFormatter("world1" ,current_column=2 , current_row=2)
   # Creating Excel Writer Object from Pandas  
json_file = open("output_file.json",'r')
data = json.load(json_file)
worksheet_name=branches["branch-name"]
s=excel.add_sheet(worksheet_name)


excel.branch_body(json_file=branches)
excel.save_excel()