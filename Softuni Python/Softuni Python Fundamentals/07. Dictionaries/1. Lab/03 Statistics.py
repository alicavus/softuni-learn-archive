
products = dict()

products.keys

while True:
    product_info = input()

    if product_info == "statistics":
        break

    product_name, product_quantity = product_info.split(": ")
    product_quantity = int(product_quantity)

    if product_name in products:
        products[product_name] += product_quantity
    else:
        products[product_name] = product_quantity

print("Products in stock:",\
    "\n".join([f'- {product_name}: {products[product_name]}' for product_name in products ]),\
    f"Total Products: {len(products.keys())}",
    f"Total Quantity: {sum(products.values())}",
    sep="\n"
)
           