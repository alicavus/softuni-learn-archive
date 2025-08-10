daily_food_gr = 300
hay_food_ratio = 0.05

weight_to_cover_ratio = 3

month_days= 30

quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
guinea_weight_in_kilograms = float(input())

quantity_food_in_grams = quantity_food_in_kilograms * 1000
quantity_hay_in_grams = quantity_hay_in_kilograms * 1000
quantity_cover_in_grams = quantity_cover_in_kilograms * 1000
guinea_weight_in_grams = guinea_weight_in_kilograms * 1000

is_terminated = False

for day in range(1, 31):
    
    quantity_food_in_grams -= daily_food_gr

    if day % 2 == 0:
        quantity_hay_in_grams -= quantity_food_in_grams * hay_food_ratio
    if day % 3 == 0:
        quantity_cover_in_grams -= guinea_weight_in_grams / weight_to_cover_ratio
        
    if quantity_food_in_grams <= 0 or quantity_hay_in_grams <= 0 or  quantity_cover_in_grams <= 0:
        print("Merry must go to the pet store!")
        break
    
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_grams / 1000:.2f}, Hay: {quantity_hay_in_grams / 1000:.2f}, Cover: {quantity_cover_in_grams / 1000:.2f}.")
