while True:
    inp = input()
    if inp == 'SoftUni':
        continue
    elif inp == 'End':
        break
    for c in inp:
        print(f'{c}{c}', end='')
    print()
