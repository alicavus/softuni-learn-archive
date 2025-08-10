group_size = int(input())

days_of_adventure = int(input())

total_coins = 0

for day in range(1, days_of_adventure+1):

    if not day % 10:
        group_size -= 2

    if not day % 15:
        group_size += 5
        total_coins -= group_size * 2

    if not day % 3:
        total_coins -= group_size * 3

    if not day % 5:
        total_coins += group_size * 20
    
    total_coins += 50
    total_coins -= group_size * 2
    

print(f"{group_size} companions received {total_coins // group_size} coins each.")
