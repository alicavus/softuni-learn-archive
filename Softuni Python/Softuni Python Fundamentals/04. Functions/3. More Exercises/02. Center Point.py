from math import floor

x1, y1, x2, y2 = [float(input()) for _ in range(4)]

d1 = x1 ** 2 + y1 **2
d1 **= 0.5

d2 = x2 ** 2 + y2 **2
d2 **= 0.5


x, y = [x1, y1] if d1 <= d2 else [x2, y2]

print(f'({floor(x)}, {floor(y)})')