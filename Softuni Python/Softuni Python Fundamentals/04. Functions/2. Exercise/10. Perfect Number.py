def is_perfect(number: int) -> bool:
    return sum(divisors(number)) == number

def divisors(number: int) -> list:
    res = []
    for divisor in range(1, number//2 + 1):
        if not number % divisor:
            res.append(divisor)
    return res

print("We have a perfect number!" if is_perfect(int(input())) else "It's not so perfect.")