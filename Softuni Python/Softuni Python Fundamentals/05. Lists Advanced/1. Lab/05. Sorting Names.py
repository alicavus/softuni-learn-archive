names = input().split(', ')

names.sort(key = lambda a : (-len(a), a))


print(names)