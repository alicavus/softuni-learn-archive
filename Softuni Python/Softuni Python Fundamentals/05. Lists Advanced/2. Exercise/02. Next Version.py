maj, min, patch = [int(x) for x in input().split('.')]

patch += 1

if patch == 10:
    min += 1
    patch = 0

if min == 10:
    maj += 1
    min = 0

print(f'{maj}.{min}.{patch}')