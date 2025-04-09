import xmltodict

xml_data = open("payments.xml").read()
data_dict = xmltodict.parse(xml_data)
root = data_dict['employees']
employees = root['employee']
lst = {}

for i in employees:
    lst.setdefault(i['name'], i['job_title'])

sorted_job = sorted(lst.values())
extract_list = []
for i in sorted_job:
    if i == 'Python Developer':
        for k, v in lst.items():
            if i == v:
                extract_list.append({'name': k, 'job': v})
final_output = {
    'employees': {
        'employee': extract_list
    }
}
with open("job.xml", "w", encoding="utf-8") as f:
    f.write(xmltodict.unparse(final_output, pretty=True))
