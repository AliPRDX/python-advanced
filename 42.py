import xmltodict

xml_data = open("payments.xml").read()
data_dict = xmltodict.parse(xml_data)
root = data_dict['employees']
employees = root['employee']
lst = {}

for i in employees:
    lst.setdefault(i['name'], i['age'])
under_30 = sorted(lst.values())
extract_list = []
for i in under_30:
    if int(i) <= 30:
        for k, v in lst.items():
            if i == v:
                extract_list.append({'name': k, 'age': v})
final_output = {
    'employees': {
        'employee': extract_list
    }
}
with open("age_under_30.xml", "w", encoding="utf-8") as f:
    f.write(xmltodict.unparse(final_output, pretty=True))
