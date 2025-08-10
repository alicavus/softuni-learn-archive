def grocery_store(**kwargs):
    return "\n".join([f"{name}: {quantity}" for name, quantity in sorted(kwargs.items(), key=lambda item:(-item[1], -len(item[0]), item[0]))])
