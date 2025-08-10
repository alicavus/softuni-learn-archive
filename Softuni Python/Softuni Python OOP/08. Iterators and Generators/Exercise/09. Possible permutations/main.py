def possible_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for i in range(len(elements)):
            rest = elements[:i] + elements[i+1:]
            for perm in possible_permutations(rest):
                yield [elements[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]