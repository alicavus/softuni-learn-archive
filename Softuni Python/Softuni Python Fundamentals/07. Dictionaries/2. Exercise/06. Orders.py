products = {}

while True:
    products_info = input()

    if products_info == "buy":
        for product in products:
            print(f'{product} -> {products[product]["quantity"] * products[product]["price"]:.2f}')
        break

    products_info_list = products_info.split()

    name, price, quantity = products_info_list[0], float(products_info_list[1]), int(products_info_list[2])

    if name not in products:
        products[name] = {
            "price": 0,
            "quantity": 0
        }
    
    products[name]["price"] = price
    products[name]["quantity"] += quantity
