def order(product: str, quantity: int) -> str:
    products = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    return(f"{products[product] * quantity:.2f}")

print(order(input(), int(input())))
