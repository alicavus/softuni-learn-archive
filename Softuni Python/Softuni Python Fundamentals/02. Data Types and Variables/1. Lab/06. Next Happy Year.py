year = str(int(input()) + 1)


while len(set([x for x in year])) < len(year):
    year = str(int(year) + 1)

print(year)