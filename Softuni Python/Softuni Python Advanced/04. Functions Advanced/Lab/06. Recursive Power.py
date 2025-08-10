def recursive_power(number, power):
    if power == 0:
        return 1
    elif power < 0:
        return recursive_power(1 / number, -power)
    return number * recursive_power(number, power - 1)