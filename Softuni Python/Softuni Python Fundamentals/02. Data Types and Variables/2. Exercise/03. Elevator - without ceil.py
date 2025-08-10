number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people // elevator_capacity

courses += 1 if number_of_people % elevator_capacity else 0

print(courses)

