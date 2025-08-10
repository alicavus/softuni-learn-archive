
efficiencies = [int(input()) for _ in range(3)]

students_count = int(input())

time_to_answer = 0

while students_count > 0:
    time_to_answer += 1
    
    if not time_to_answer % 4:
        continue

    students_count -= sum(efficiencies)

print(f"Time needed: {time_to_answer}h.")
