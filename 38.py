import xml.etree.ElementTree as ET


def extract_names():
    with open("payments.xml") as f:
        data = ET.parse(f)
        root = data.getroot()
    for i in root.iter("employee"):
        name = i.find('name').text
        job = i.find('job_title').text
        print("name = ", name, " ", "job = ", job)


extract_names()
