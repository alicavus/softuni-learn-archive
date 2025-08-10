my_numbers = [int(x) for x in input().split(", ")]

print(f"""Positive: {", ".join(str(x) for x in my_numbers if x >= 0)}
Negative: {", ".join(str(x) for x in my_numbers if x < 0)}
Even: {", ".join(str(x) for x in my_numbers if not x % 2)}
Odd: {", ".join(str(x) for x in my_numbers if x % 2)}""")