number_str = input()
print(f"Odd sum = {sum([int(x) for x in number_str if int(x) % 2])}, Even sum = {sum([int(x) for x in number_str if not int(x) % 2])}")