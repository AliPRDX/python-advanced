import xml.etree.ElementTree as ET


def extract_names():
    with open("payments.xml") as f:
        root = xml_dict["bookstore"]
        books = root["book"]
    for i in root.iter("employee"):
        name = i.find('name').text
        job = i.find('job_title').text
        print("name = ", name, " ", "job = ", job)


extract_names()
