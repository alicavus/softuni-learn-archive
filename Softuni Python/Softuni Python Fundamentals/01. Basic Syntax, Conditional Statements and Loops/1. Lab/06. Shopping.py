budget = int(input())

cmd = input()

while cmd != "End":
    budget -= int(cmd)
    if budget < 0:
        print(f'You went in overdraft!')
        break
    cmd = input()

else:
    print(f'You bought everything needed.')