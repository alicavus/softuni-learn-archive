def rotate_once(l: list) -> list:
    new_list = []
    half_of_the_dec = len(l) // 2
    for idx in range(half_of_the_dec):
        new_list += [l[idx], l[idx+half_of_the_dec]]
    return new_list

    

my_dec_of_cards = input().strip().split(' ')
shuffle_count = int(input())

for _ in range(shuffle_count):
   my_dec_of_cards = rotate_once(my_dec_of_cards)

print(my_dec_of_cards)

