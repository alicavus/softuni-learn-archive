def sign_of_multiplication(l: list[float]) -> str:
    
    if 0.0 in l:
        return 'zero'
    
    res = 'positive'
    
    for n in l:
        if n > 0:
            continue
        res = 'positive' if res == 'negative' else 'negative'
    
    return res


numbers = [float(input()) for x in 'abc']

print(sign_of_multiplication(numbers))