def is_prime(n: int) -> bool:
    for num in range(2, n//2 + 1):
        if not n % num:
            return False
    return True

print(is_prime(int(input())))