def shop_from_grocery_list(shopping_budget: int, grocery_list: list[str], *args) -> str:
    grocery_shop = []
    budget = shopping_budget * 1.0
    for shopping_item in args:
        if shopping_item[0] not in grocery_list:
            continue
        elif shopping_item[1] <= budget:
            grocery_list.remove(shopping_item[0])
            grocery_shop.append(shopping_item[0])
            budget -= shopping_item[1]
        else:
            break

    result = []

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return "You did not buy all the products. Missing products: " + ", ".join(grocery_list) + "."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

print(shop_from_grocery_list(
            100,
            ["tomato", "cola", "chips", "meat"],
            ("cola", 5.8),
            ("tomato", 10.0),
            ("meat", 22)))

