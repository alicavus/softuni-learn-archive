text = input()

try:
    print(text * int(input()))
except ValueError:
    print("Variable times must be an integer")