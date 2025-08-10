for _ in range(int(input())):
    txt = input()
    purity = 'pure.' if all([x not in ',._' for x in txt]) else 'not pure!'
    print(f'{txt} is {purity}')
