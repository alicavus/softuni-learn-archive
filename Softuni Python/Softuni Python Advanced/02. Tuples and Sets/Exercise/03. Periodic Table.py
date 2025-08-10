chemicals = set()
for _ in range(int(input())):
    for chemical in input().split():
        chemicals.add(chemical)

for chemical in chemicals:
    print(chemical)