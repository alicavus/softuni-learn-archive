def print_a_b(a: int, b: int, c: str):
    print(f"""{c}:
a = {a}
b = {b}""")

a, b = [int(input()) for _ in "ab"]

print_a_b(a, b, "Before")

tmp = a
a = b
b = tmp

print_a_b(a, b, "After")

