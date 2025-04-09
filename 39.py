import xmltodict


def extract_names():
    payment = []
    with open("payments.xml") as f:
        data = ET.parse(f)
        root = data.getroot()
    for i in root.iter("employee"):
        monthly_payment = i.find('monthly_payment')
        for month in monthly_payment:
            payment.append(int(month.text.strip()))

    avg = sum(payment) / len(payment)
    return avg


print(extract_names())
