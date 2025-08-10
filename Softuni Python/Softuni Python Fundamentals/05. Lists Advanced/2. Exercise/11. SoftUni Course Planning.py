schedule = input().split(", ")

while True:
    command_line = input()
    if command_line == "course start":
        for idx, lesson in enumerate(schedule, 1):
            print(f"{idx}.{lesson}")
        break

    commands = command_line.split(":")

    match commands[0]:
        case "Add":
            lesson = commands[1]
            if lesson not in schedule:
                schedule.append(lesson)
        case "Insert":
            lesson = commands[1]
            idx = int(commands[2])

            if lesson not in schedule:
                schedule.insert(idx, lesson)
        
        case "Remove":
            lesson = commands[1]
            if lesson in schedule:
                if f'{lesson}-Exercise' in schedule:
                    exercise_idx = schedule.index(f'{lesson}-Exercise')
                    schedule.pop(exercise_idx)
                idx = schedule.index(lesson)
                schedule.pop(idx)
        
        case "Swap":
            lesson_one = commands[1]
            lesson_two = commands[2]

            if lesson_one in schedule and lesson_two in schedule:
                idex_one = schedule.index(lesson_one)
                idex_two = schedule.index(lesson_two)
                    
                schedule[idex_one], schedule[idex_two] = schedule[idex_two], schedule[idex_one]

                if f'{lesson_one}-Exercise' in schedule:
                    schedule.remove(f'{lesson_one}-Exercise')
                    idex_one = schedule.index(lesson_one)
                    schedule.insert(idex_one+1, f'{lesson_one}-Exercise')

                if f'{lesson_two}-Exercise' in schedule:
                    schedule.remove(f'{lesson_two}-Exercise')
                    idex_two = schedule.index(lesson_two)
                    schedule.insert(idex_two+1, f'{lesson_two}-Exercise')
                
        
        case "Exercise":
            lesson = commands[1]
            if lesson in schedule:
                idx = schedule.index(lesson)
                if f'{lesson}-Exercise' not in schedule:
                    schedule.insert(idx+1, f'{lesson}-Exercise')
            else:
                schedule.append(lesson)
                if f'{lesson}-Exercise' not in schedule:
                    schedule.append(f'{lesson}-Exercise')