neighborhood_love_needs = list(map(int, input().split("@")))
cupid_love_need_decrease = 2

cupid_idx = 0

while True:
    cupid_action = input()

    if cupid_action == "Love!":
        print(f"Cupid's last position was {cupid_idx}.")
        if sum(neighborhood_love_needs):
            print(f"Cupid has failed {len(list(filter(int, neighborhood_love_needs)))} places.")
        else:
            print("Mission was successful.")
            
        break

    steps = int(cupid_action.split()[1])

    cupid_idx += steps

    if cupid_idx not in range(len(neighborhood_love_needs)):
        cupid_idx = 0
    
    if neighborhood_love_needs[cupid_idx] == 0:
        print(f"Place {cupid_idx} already had Valentine's day.")
        continue
    
    neighborhood_love_needs[cupid_idx] -= cupid_love_need_decrease
    
    if neighborhood_love_needs[cupid_idx] == 0:
        print(f"Place {cupid_idx} has Valentine's day.")
        