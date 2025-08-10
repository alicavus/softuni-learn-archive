number = float(input())

if number == 0:
    res = "zero"
elif number > 0:
    res = "positive"
else:
    res = "negative"

if 0 < abs(number) < 1:
    res = f'small {res}'
elif abs(number) > 1000000:
    res = f'large {res}'

print(res)
