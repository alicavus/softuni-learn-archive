
budget = float(input())
price_per_kg_flour = float(input())

egg_package_price = price_per_kg_flour * 0.75
milk_price_per_liter = price_per_kg_flour * 1.25
milk_price_per_bread = milk_price_per_liter * 0.25

breads_count = 0
colored_eggs_count = 0

while budget >= (egg_package_price + price_per_kg_flour + milk_price_per_bread):
    budget -= (egg_package_price + price_per_kg_flour + milk_price_per_bread)
    
    breads_count += 1
    colored_eggs_count += 3
    
    if breads_count % 3 == 0:
        colored_eggs_count -= (breads_count - 2)
        
print(f"You made {breads_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")




