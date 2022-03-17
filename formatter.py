import json
from json_generator.processing.issue_processing.parsing_component import parse_list_json_issues_to_list_json_objects
from pdf_generator.Body import PdfFormatter
from json_generator.models.issue import Component



pdf = PdfFormatter('P', 'mm' , 'Letter')

pdf.set_auto_page_break(
    auto=True , margin=15
)
print('the pdf is : '+str(pdf.w))

# pdf.add_page()

#print data for each file : 

json_file = open('output_file.json','r')
data = json.load(json_file)
file = Component(key=None)
file.parse_jsoncomponent_from_output_file(data[0]["details"][0]["information_per_file"][0])
issues_json = data[0]["details"][0]["information_per_file"][0]["issues"]

unresolved = list(issues_json["unresolved"])
# print("the unresolved are : "+json.loads(str(unresolved[0]))["key"])

wontfix = list(issues_json["wontfix"])

fixed = list(issues_json["fixed"])

false_positive = list(issues_json["false_positive"])

removed = list(issues_json["removed"])

unresolved_issues = parse_list_json_issues_to_list_json_objects(unresolved)
wontfix_issues = parse_list_json_issues_to_list_json_objects(wontfix)
fixed_issues = parse_list_json_issues_to_list_json_objects(fixed)
false_positive_issues = parse_list_json_issues_to_list_json_objects(false_positive)
removed_issues = parse_list_json_issues_to_list_json_objects(removed)


pdf.first_page()
pdf.ln(20)
# pdf.add_page()
pdf.set_auto_page_break(auto=True,margin =15)

pdf.second_page('output_file.json')
# # print("the uuid of file is : "+str(data[0]["details"][0]["information_per_file"]))
pdf.add_page()
pdf.summaryHeader(title='Informations about the file')
pdf.add_file(file , unresolved_issues=unresolved_issues,wontfix_issues=wontfix_issues ,fixed_issues=fixed_issues , false_positive_isssues=false_positive_issues , removed_issues=removed_issues)

#swl wach najotiw les tags tahoma ola blach 

pdf.output('report.pdf')

#