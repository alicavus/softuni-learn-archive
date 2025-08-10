from collections import deque

money = [int(x) for x in input().split()]
foods = deque([int(x) for x in input().split()])

ate_foods = 0

while money and foods:
    current_money = money.pop()
    current_food = foods.popleft()

    if current_money == current_food:
        ate_foods += 1

    elif current_money > current_food:
        ate_foods += 1
        current_money -= current_food

        if money:
            money[-1] += current_money
        else:
            money.append(current_money)

if ate_foods >= 4:
    print(f'Gluttony of the day! Henry ate {ate_foods} foods.')

elif ate_foods >= 1:
    print(f'Henry ate: {ate_foods} food{"s" if ate_foods > 1 else ""}.')

else:
    print('Henry remained hungry. He will try next weekend again.')