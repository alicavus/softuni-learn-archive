from collections import deque

food_quantity = int(input())

food_orders = deque([int(x) for x in input().split()])

biggest_order = max(food_orders)

print(biggest_order)

while food_orders:
    curr_order = food_orders[0]

    if food_quantity >= curr_order:
        food_quantity -= food_orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in food_orders])}")
        break
else:
    print("Orders complete")
