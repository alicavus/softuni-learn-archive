try:
    for _ in range(int(input())):
        number = int(input())
        if number % 2:
            print(f'{number} is odd!')
            exit()
    else:
        print('All numbers are even.')
except:
    pass