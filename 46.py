import csv

avg_stu = {
    "ali": 19,
    "mamad": 20,
    "mobin": 18,
    "parham": 17
}
with open("st.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["name", "avg"])
    for name, avg in avg_stu.items():
        csv_writer.writerow([name, avg])
