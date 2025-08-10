def squares(number):
    curr = 1
    while curr <= number:
        yield curr ** 2
        curr += 1



print(list(squares(5)))
