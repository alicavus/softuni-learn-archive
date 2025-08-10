odd_set = set()
even_set = set()

for idx in range(int(input())):
    cur_row = idx + 1
    cur_sum = sum([ord(x) for x in input()])
    cur_sum //= cur_row

    if not cur_sum % 2:
        even_set.add(cur_sum)
        continue
    odd_set.add(cur_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(", ".join(map(str, odd_set.union(even_set))))
elif odd_sum > even_sum:
    print(", ".join(map(str, odd_set.difference(even_set))))
else:
    print(", ".join(map(str, odd_set.symmetric_difference(even_set))))