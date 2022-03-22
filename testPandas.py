import json
import csv
from operator import index
import pandas as pd 
import openpyxl
import xlsxwriter


df = pd.read_json("output_file.json")
summary_dataframe=pd.DataFrame(df.details[0])["summary_informations"]
sum_list=summary_dataframe.tolist()
data_2=pd.DataFrame.from_records(sum_list)


#data2 is a frame of 3 columns(branch-name, date-last, unresolved-issues)

# print(data_2["unresolved-issues"])
issues_list=data_2["unresolved-issues"].tolist()
data_3=pd.DataFrame.from_records(issues_list)
#data3 is a  frame of  2 columns (total, issues-details)
print(type(data_3["total"]))
details_issues=data_3["issues-details"].tolist()
data_4=pd.DataFrame.from_records(details_issues)
print(data_4) 

#data4 is a frame of 2 columns (category, severity)

category_list=data_4["category"].tolist()
data_5=pd.DataFrame.from_records(category_list)
print(data_5)

severity_list=data_4["severity"].tolist()
data_6=pd.DataFrame.from_records(severity_list)
print(data_6)

# data_2.to_excel("out.xlsx")