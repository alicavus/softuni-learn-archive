foods = dict()

total_sold_quantity = 0

while True:
    cmd = input()
    
    if cmd == "Complete":
        break
    
    cmd_list = cmd.split(" ")

    command = cmd_list[0]
    quantity = int(cmd_list[1])
    food = cmd_list[2]

    match command:
        case "Receive":
            if quantity <= 0:
                continue
            if food not in foods:
                foods.update({food: quantity})
            else:
                foods[food] += quantity
        case "Sell":
            if food not in foods:
                print(f"You do not have any {food}.")
                continue
            if foods[food] < quantity:
                quantity = foods[food]
                print(f"There aren't enough {food}. You sold the last {quantity} of them.")
            else:
                print(f"You sold {quantity} {food}.")
            
            foods[food] -= quantity
            if not foods[food]:
                foods.pop(food)
            total_sold_quantity += quantity
        case _:
            pass

for food in foods:
    print(f"{food}: {foods[food]}")

print(f"All sold: {total_sold_quantity} goods")
    
            
