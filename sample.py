# print the highest order id , profit and product name

import csv


def unique_orders(csv_file):
    orders = {}

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            order_id = row['Order ID']
            profit = float(row['Profit'])
            product_name = row['Product Name']

            if order_id not in orders:
                orders[order_id] = {'profit': profit, 'products': [product_name]}
            else:
                if profit > orders[order_id]['profit']:
                    orders[order_id]['profit'] = profit
                orders[order_id]['products'].append(product_name)

    for order_id, data in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Highest Profit: {data['profit']}")
        print("Product Names:")
        for product_name in set(data['products']):
            print(product_name)
        print()


# Example usage
csv_file_path = 'Walmart.csv'

try:
    unique_orders(csv_file_path)
except FileNotFoundError:
    print("CSV file not found.")





















