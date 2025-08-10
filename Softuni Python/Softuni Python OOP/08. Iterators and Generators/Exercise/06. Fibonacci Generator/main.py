def fibonacci():
    cur, prev = 1, 0
    while True:
        yield prev
        prev, cur = cur, prev+cur



generator = fibonacci()
for i in range(5):
    print(next(generator))
