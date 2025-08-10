quantity_of_decorations = int(input())
days_left = int(input())

DECORATIONS = {
    "Ornament Set": {
        "price": 2,
        "points": 5
    },
    "Tree Skirt": {
        "price": 5,
        "points": 3
    },
    "Tree Garland": {
        "price": 3,
        "points": 10
    },
    "Tree Lights": {
        "price": 15,
        "points": 17
    }
}

budget = 0
spirit = 0

for day in range(1, days_left + 1):
    if day == days_left and not days_left % 10:
        spirit -= 30
    
    if not day % 11:

        quantity_of_decorations += 2

    if not day % 10:
        spirit -= 20

        budget += DECORATIONS["Tree Skirt"]["price"]
        budget += DECORATIONS["Tree Garland"]["price"]
        budget += DECORATIONS["Tree Lights"]["price"]

    if not day % 5:
        budget += DECORATIONS["Tree Lights"]["price"] * quantity_of_decorations
        spirit += DECORATIONS["Tree Lights"]["points"]

        if not day % 3:
            spirit += 30

    if not day % 3:
        budget += DECORATIONS["Tree Skirt"]["price"] * quantity_of_decorations
        spirit += DECORATIONS["Tree Skirt"]["points"]

        budget += DECORATIONS["Tree Garland"]["price"] * quantity_of_decorations
        spirit += DECORATIONS["Tree Garland"]["points"]

    if not day % 2:
        budget += DECORATIONS["Ornament Set"]["price"] * quantity_of_decorations
        spirit += DECORATIONS["Ornament Set"]["points"]


print(f"""Total cost: {budget}
Total spirit: {spirit}""")