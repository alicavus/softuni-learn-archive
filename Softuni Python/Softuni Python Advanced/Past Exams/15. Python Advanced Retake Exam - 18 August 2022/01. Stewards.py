from collections import deque

seats = input().split(", ")

first_sequence = deque(map(int, input().split(", ")))
second_sequence = deque(map(int, input().split(", ")))

taken_seats = []

MAX_ROTATIONS = 10
GOAL_TAKEN_SEATS = 3

rotations = 0

while rotations < MAX_ROTATIONS and len(taken_seats) < GOAL_TAKEN_SEATS:
    rotations += 1
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    char = chr(first_number + second_number)

    first_seat, second_seat = f'{first_number}{char}', f'{second_number}{char}'

    if first_seat not in seats and second_seat not in seats:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)
    
    else:
        for seat in [first_seat, second_seat]:
            if seat in seats:
                if seat not in taken_seats:
                    taken_seats += [seat]

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
    