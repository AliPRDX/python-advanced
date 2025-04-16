import csv
import json

with open("customer_orders.json", "r") as f:
    customer_orders = json.load(f)
customer_orders_csv = [
    ["customer_name", "order_id", "items", "order_date", "price_per_item", "total_price"]
]

for i in customer_orders["orders"]:
    number = len(i["items"])

    for j in range(number):
        data = [i["customer"]["name"], i["order"]["order_id"], i["items"][j]["product_name"], i["order"]["order_date"],
                i["items"][j]["price_per_item"], i["order"]["total_price"]]
        customer_orders_csv.append(data)

with open("customer_orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(customer_orders_csv)
    print("Done")
