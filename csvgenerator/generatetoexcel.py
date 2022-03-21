import json
import csv
import pandas as pd 

df = pd.read_json("output_file.json")
bn=pd.DataFrame(df.details[0])['summary_informations']
print(bn)

# print(df)
# # df.to_excel("out.xlsx")

