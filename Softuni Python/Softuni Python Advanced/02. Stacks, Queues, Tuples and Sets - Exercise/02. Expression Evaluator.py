from collections import deque

expression = deque(input().split())
clipboard = deque()

while len(expression) > 1:
    while expression and expression[0] not in "*/+-":
        clipboard.append(expression.popleft())

    cur_value = int(clipboard.popleft())

    while clipboard:
        right_number = int(clipboard.popleft())
        match expression[0]:
            case "*":
                cur_value *= right_number
            case "/":
                cur_value //= right_number
            case "+":
                cur_value += right_number
            case "-":
                cur_value -= right_number
    
    expression.popleft()
    expression.appendleft(str(cur_value))

print(expression[0])
