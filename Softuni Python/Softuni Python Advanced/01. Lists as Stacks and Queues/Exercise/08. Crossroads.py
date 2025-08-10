from collections import deque

greenlight_duration = int(input())
free_window_duration = int(input())

processed_cars = []
car_queue = deque()

while True:
    command = input()

    if command.lower() == "end":
        print(f"Everyone is safe.\n{len(processed_cars)} total cars passed the crossroads.")
        break

    elif command.lower() == "green":
        green_time = greenlight_duration
        window_time = free_window_duration

        while car_queue and green_time > 0:
            car = car_queue.popleft()
            car_time = len(car)

            if car_time <= green_time:
                green_time -= car_time
                processed_cars.append(car)
            elif car_time <= green_time + window_time:
                processed_cars.append(car)
                break
            else:
                hit_char = car[green_time + window_time]
                print(f"A crash happened!\n{car} was hit at {hit_char}.")
                exit()

    else:
        car_queue.append(command)
