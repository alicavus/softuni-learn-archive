from re import findall

def remove_empty(l: list[list]) -> list:
    r = []
    for ll in l:
        ll = list(filter(len, ll))
        r.append(ll)
    return r


expression = r'#([a-zA-Z\s]+)#(\d{2}/\d{2}/\d{2})#(\d{1,5})#|\|([a-zA-Z\s]+)\|(\d{2}/\d{2}/\d{2})\|(\d{1,5})\|'

food_info_string = input()

food_info_results = findall(expression, food_info_string)

food_info_results = remove_empty(food_info_results)

total_calories = 0

for food_result in food_info_results:
    total_calories += int(food_result[2])

print(f"You have food to last you for: {total_calories // 2000} days!")

for food_result in food_info_results:
    print(f"Item: {food_result[0]}, Best before: {food_result[1]}, Nutrition: {food_result[2]}")