office_happiness_values = [int(x) for x in input().split()]
factor = int(input())

office_happiness_values = list(map(lambda x: x*factor, office_happiness_values))
average_happiness = sum(office_happiness_values) / len(office_happiness_values)
happy_emploees = [x for x in office_happiness_values if x >= average_happiness]

is_office_happy = True if len(happy_emploees) >= len(office_happiness_values) / 2 else False

print(f"Score: {len(happy_emploees)}/{len(office_happiness_values)}. Employees are {'not ' if not is_office_happy else ''}happy!")