MAX_HEALTH = 100

health = MAX_HEALTH
bitcoins = 0

dungeon = input().split("|")

max_room = 0

for room_idx in range(len(dungeon)):
    cur_room = dungeon[room_idx]
    quest = cur_room.split()

    if quest[0] == "potion":
        quest_health_points = int(quest[1])
        if health + quest_health_points > MAX_HEALTH:
            quest_health_points = MAX_HEALTH - health
        health += quest_health_points
        print(f"You healed for {quest_health_points} hp.")
        print(f"Current health: {health} hp.")
    
    elif quest[0] == "chest":
        bitcoins += int(quest[1])
        print(f"You found {quest[1]} bitcoins.")
    
    else:
        monster, attack = quest[0], int(quest[1])

        health -= attack

        if health <= 0:
            print(f"You died! Killed by {monster}.\nBest room: {room_idx+1}")
            break
        print(f"You slayed {monster}.")
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")