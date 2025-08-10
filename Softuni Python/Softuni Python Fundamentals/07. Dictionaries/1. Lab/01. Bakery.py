
food_info = input()

food_dict = dict()

food_names = [x for x in food_info.split() if x.isalpha()]
food_quantities = [int(x) for x in food_info.split() if x.isdigit()]

for food, quantity in zip(food_names, food_quantities):
    food_dict.update({food: quantity})

print(food_dict)
