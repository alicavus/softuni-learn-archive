train_ticket = 150

collection_of_items = input().strip().split("|")

budget = float(input())

prices = {
    "Clothes": 50.0,
    "Shoes": 35.0,
    "Accessories": 20.5
}

items_to_sell = []

total_price =  0

for item in collection_of_items:
    item_type = item.split("->")[0]
    item_price = float(item.split("->")[1])

    if item_price > prices[item_type] or budget < item_price:
        continue

    budget -= item_price

    items_to_sell += [item_price * 1.4]
    
    total_price += item_price

sum_of_sell_items = sum(items_to_sell)
profit = sum_of_sell_items - total_price

budget += sum_of_sell_items

print(" ".join([f'{x:.2f}' for x in items_to_sell]))
print(f"Profit: {profit:.2f}")

print("Hello, France!" if budget >= train_ticket else "Not enough money.")

