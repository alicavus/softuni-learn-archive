positive_numbers = []
negative_numbers = []

for _ in range(int(input())):
    n = int(input())
    if n >= 0:
        positive_numbers += [n]
    else:
        negative_numbers += [n]

print(positive_numbers, negative_numbers, sep="\n")

print(f"Count of positives: {len(positive_numbers)}", f"Sum of negatives: {sum(negative_numbers)}", sep="\n")