
parking_lot = set()

for _ in range(int(input())):
    car_direction, car_number = input().split(", ")
    if car_direction.lower() == "in":
        if car_number in parking_lot:
            continue
        parking_lot.add(car_number)
    elif car_direction.lower() == "out":
        if car_number not in parking_lot:
            continue
        parking_lot.remove(car_number)

if parking_lot == set():
    print("Parking Lot is Empty")
else:
    for car_number in parking_lot:
        print(car_number)
