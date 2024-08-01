import csv

# Read master_product.csv and store the records in a dictionary with ID as the key
master_product = {}
with open('master_product.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        master_product[row['ID']] = row

# Read product.csv to get the list of IDs
product_ids = []
with open('product.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_ids.append(row['ID'])

# Filter the records from master_product based on product_ids and write to output.csv
with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['ID', 'Product Name', 'Customer Name','Price', 'GST %']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for product_id in product_ids:
        if product_id in master_product:
            writer.writerow(master_product[product_id])

print("Filtered records have been written to output.csv")
