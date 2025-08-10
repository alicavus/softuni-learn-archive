from collections import deque

def do_math(left: int, op: str, right: int) -> int:
    result = 0
    match op:
        case "+":
            result = left + right
        case "-":
            result = left - right
        case "*":
            result = left * right
        case "/":
            result = left / right
    
    return abs(result)


bees = deque([int(bee) for bee in input().split()])
nectar = deque([int(bee) for bee in input().split()])

symbols = deque(input().split())

honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar[-1]

    while nectar and current_nectar < current_bee:
        nectar.pop()
        if nectar:
            current_nectar = nectar[-1]
    
    if current_nectar < current_bee:
        break

    current_symbol = symbols.popleft()

    if current_symbol == "/" and current_nectar == 0:
        pass
    else:
        current_honey = do_math(current_bee, current_symbol, current_nectar)
        honey += current_honey
    bees.popleft()
    nectar.pop()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

elif nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

