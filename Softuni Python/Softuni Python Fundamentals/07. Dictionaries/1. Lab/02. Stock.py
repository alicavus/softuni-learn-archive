
food_info = input()

food_dict = dict()

food_names = [x for x in food_info.split() if x.isalpha()]
food_quantities = [int(x) for x in food_info.split() if x.isdigit()]

for food, quantity in zip(food_names, food_quantities):
    food_dict[food] = quantity

for food in input().split():
    if food in food_dict:
        print(f'We have {food_dict[food]} of {food} left')
    else:
        print(f'Sorry, we don\'t have {food}')

