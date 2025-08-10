def add_or_multiply(a: float, b: float)-> float:
    if b == 0:
        return a * 0.8
    return a+b

sequence_of_numbers = [int(x) for x in input().strip().split(' ')]

left_cars_time = 0.0
right_cars_time = 0.0

winner = {"car": "", "time": 0}

for idx in range(len(sequence_of_numbers)//2):
    cur_left_point = sequence_of_numbers[idx]
    cur_right_point = sequence_of_numbers[-(idx+1)]

    left_cars_time = add_or_multiply(left_cars_time, cur_left_point)
    right_cars_time = add_or_multiply(right_cars_time, cur_right_point)

    winner['car'] = 'left' if left_cars_time < right_cars_time else 'right'
    winner['time'] = left_cars_time if left_cars_time < right_cars_time else right_cars_time

print(f'The winner is {winner["car"]} with total time: {winner["time"]:.1f}')