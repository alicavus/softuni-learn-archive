def cookbook(*args):
    recipe_categories = {}

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in recipe_categories:
            recipe_categories[cuisine] = []
        recipe_categories[cuisine].append((recipe_name, ingredients))

    sorted_recipe_categories = sorted(recipe_categories.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for cuisine, recipes in sorted_recipe_categories:
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        result += f"{cuisine} cuisine contains {len(sorted_recipes)} recipes:\n"
        for recipe_name, ingredients in sorted_recipes:
            result += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"
    return result.strip()


# Example usage:
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))


# print(cookbook(("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])))


# print(cookbook(("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#                       ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
#                       ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
#                       ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#                       ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
#                       ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
#                       ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
#                       ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))


