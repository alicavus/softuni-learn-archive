from collections import deque

money = list(map(int, input().split()))
prices = deque(map(int, input().split()))

# Initialize a counter to keep track of the number of foods Henry eats
count = 0

# Loop until there's no more money or prices
while money and prices:
    # Get the current amount of money and price
    current_money = money[-1]
    current_price = prices[0]

    # Check if Henry can buy the food with the current money
    if current_money == current_price:
        # Henry buys the food, remove money and price, and increase the count
        money.pop()
        prices.popleft()
        count += 1
    elif current_money > current_price:
        # Calculate the change, update money, remove price, and increase the count
        change = current_money - current_price
        money.pop()
        if money:
            money[-1] += change
        prices.popleft()
        count += 1
    else:
        # Henry cannot afford the food, remove both money and price
        money.pop()
        prices.popleft()


if count >= 4:
    print(f"Gluttony of the day! Henry ate {count} foods.")
elif count == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {count} food{'s' if count != 1 else ''}.")
