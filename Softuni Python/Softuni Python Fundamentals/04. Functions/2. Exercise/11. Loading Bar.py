
percent = int(input())
percent_divided = percent // 10

if 0 <= percent_divided < 10:
    print(f"""{percent}% [{'%' * percent_divided + '.' * (10 - percent_divided - 1)}.]
Still loading...""")

else:
    print("""100% Complete!
[%%%%%%%%%%]""")