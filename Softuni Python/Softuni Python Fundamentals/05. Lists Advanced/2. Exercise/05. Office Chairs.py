number_of_rooms = int(input())

chairs_balance = [0] * number_of_rooms

for room_idx in range(number_of_rooms):
    chairs, visitors = input().split()

    chairs_balance[room_idx] = len(chairs) - int(visitors)

if all([x>=0 for x in chairs_balance]):
    print(f"Game On, {sum(chairs_balance)} free chairs left")
else:
    for room_number, balance in enumerate(chairs_balance, 1):
        if balance < 0:
            print(f"{-balance} more chairs needed in room {room_number}")
