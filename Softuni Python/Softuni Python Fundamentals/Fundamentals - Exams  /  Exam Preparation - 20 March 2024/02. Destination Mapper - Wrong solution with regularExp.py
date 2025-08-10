# The difference with Judge is caused by ordering of output list

from re import findall

locations = input()



destinations = findall(r'(?<==)[A-Z]{1}[A-Za-z]{2,}(?==)', locations)
destinations += findall(r'(?<=/)[A-Z]{1}[A-Za-z]{2,}(?=/)', locations)

#destinations.sort()

print(f"""Destinations: {", ".join(destinations)}
Travel Points: {sum([len(x) for x in destinations])}""")