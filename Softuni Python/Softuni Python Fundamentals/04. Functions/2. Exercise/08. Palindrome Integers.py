def is_palindrome(number: int) -> bool:
    number_str = str(number)
    return number_str[::-1] == number_str

for number in [int(x) for x in input().strip().split(', ')]:
    print(is_palindrome(number=number))
