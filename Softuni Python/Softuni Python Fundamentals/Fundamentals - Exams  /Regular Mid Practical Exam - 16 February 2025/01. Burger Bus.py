number_of_cities = int(input())

burger_buss = []

total_earnings = 0

for idx in range(number_of_cities):
    burger_buss.append(
        {
            "city": input(),
            "earned": float(input()),
            "expences": float(input()),
            "additional expences": 0,
            "profit": 0
        }
    )
    if idx % 5 == 4:
        burger_buss[idx]["additional expences"] = 0.1 * burger_buss[idx]["earned"]
    elif idx % 3 == 2:
        burger_buss[idx]["additional expences"] = 0.5 * burger_buss[idx]["expences"]
    
    burger_buss[idx]["profit"] =  burger_buss[idx]["earned"] - burger_buss[idx]["expences"] - burger_buss[idx]["additional expences"]

    total_earnings += burger_buss[idx]["profit"]

    print(f'In {burger_buss[idx]["city"]} Burger Bus earned {burger_buss[idx]["profit"]:.2f} leva.')

print(f"Burger Bus total profit: {total_earnings:.2f} leva.")
    