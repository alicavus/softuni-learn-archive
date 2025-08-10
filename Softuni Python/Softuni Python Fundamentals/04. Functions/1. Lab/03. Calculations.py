def calculate(operator: str, a: int, b: int) -> int:
    res = None
    match operator:
        case "multiply":
            res = a * b
        case "divide":
            res = a // b
        case "add":
            res = a + b
        case "subtract":
            res = a - b
    return res

operator = input()
number_one = int(input())
number_two = int(input())

print(calculate(operator=operator, a=number_one, b=number_two))
