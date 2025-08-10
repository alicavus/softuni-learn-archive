from re import search

pattern = r''

total_price = 0.0

while True:
    order_data = input()

    if order_data == "end of shift":
        break

    customer_match = search(pattern=r'%([A-Z]{1}[a-z]+)%', string=order_data)
    product_match = search(pattern=r'\<(\w+)\>', string=order_data)
    count_match = search(pattern=r'\|(\d+)\|', string=order_data)
    price_match = search(pattern=r'(\d+(?:\.\d+)?)\$', string=order_data)

    if customer_match is None or product_match is None or count_match is None or price_match is None:
        continue

    
    customer = customer_match.group(1)
    product = product_match.group(1)
    count = int(count_match.group(1))
    price = float(price_match.group(1))

    current_price = count * price
    total_price += current_price

    print(f"{customer}: {product} - {current_price:.2f}")

print(f"Total income: {total_price:.2f}")