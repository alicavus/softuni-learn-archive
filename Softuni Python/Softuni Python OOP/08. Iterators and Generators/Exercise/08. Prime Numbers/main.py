def get_primes(collection: list[int]):
    def is_prime(number: int):
        for n in range(2, int(abs(number) ** 0.5) + 1):
            if number % n == 0:
                return False
        return number > 1
    
    for num in collection:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))



