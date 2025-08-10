from collections import deque

armor_of_the_monsters = deque([int(x) for x in input().split(",")])
soldiers_striking_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while armor_of_the_monsters and soldiers_striking_impact:
    curr_monster_armour = armor_of_the_monsters.popleft()
    curr_soldier_impact = soldiers_striking_impact.pop()

    if curr_soldier_impact >= curr_monster_armour:
        killed_monsters += 1
        curr_soldier_impact -= curr_monster_armour

        if curr_soldier_impact > 0:
            if not soldiers_striking_impact:
                soldiers_striking_impact = [0]
            soldiers_striking_impact[-1] += curr_soldier_impact

    else:
        curr_monster_armour -= curr_soldier_impact
        armor_of_the_monsters.append(curr_monster_armour)

if not armor_of_the_monsters:
    print("All monsters have been killed!")

if not soldiers_striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")




