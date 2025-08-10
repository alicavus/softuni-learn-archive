PEOPLE_PER_WAGON = 4

people_count = int(input())
lift_state = [int(x) for x in input().split(" ")]

for wagon_number in range(len(lift_state)):
    wagon = lift_state[wagon_number]
    free_spots = PEOPLE_PER_WAGON - wagon
    if free_spots:
        if people_count >= free_spots:
            lift_state[wagon_number] += free_spots
            people_count -= free_spots
        else:
            lift_state[wagon_number] += people_count
            people_count = 0
    else:
        continue

    if not people_count: break

print(f"There isn't enough space! {people_count} people in a queue!\n" if people_count else "The lift has empty spots!\n" if len(lift_state) * PEOPLE_PER_WAGON != sum(lift_state) else "", end='')

print(" ".join([str(x) for x in lift_state]))

