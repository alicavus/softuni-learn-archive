def cookbook(*args) -> str:
    recipees_dict = {}

    for recipe in args:
        name, cuisine, ingredients = recipe
        if cuisine not in recipees_dict:
            recipees_dict[cuisine] = {}
        recipees_dict[cuisine][name] = ingredients

    result = []

    for cuisine, recipe_data in sorted(recipees_dict.items(), key=lambda item: (-len(item[1].items()), item[0])):
        result += [f"{cuisine} cuisine contains {len(recipe_data)} recipes:"]
        for recipe, ingredients in sorted(recipe_data.items(), key=lambda item: item[0]):
            result += [f"  * {recipe} -> Ingredients: {', '.join(ingredients)}"]

    return "\n".join(result)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

