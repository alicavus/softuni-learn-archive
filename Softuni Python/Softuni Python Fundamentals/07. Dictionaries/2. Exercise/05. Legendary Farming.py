
precious_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk_items = {}

rewards = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

reward_threshold = 250

reward_earned = False

while not reward_earned:
    items_info = input().split()

    for item_idx in range(0, len(items_info), 2):
        item, value = items_info[item_idx+1].lower(), int(items_info[item_idx])

        if item in precious_items:
            precious_items[item] += value

            if precious_items[item] >= reward_threshold:
                precious_items[item] -= reward_threshold

                print(f'{rewards[item]} obtained!')

                for item in precious_items:
                    print(f"{item}: {precious_items[item]}")
                
                for item in junk_items:
                    print(f"{item}: {junk_items[item]}")

                reward_earned = True
                break
        
        else:
            if item not in junk_items:
                junk_items[item] = 0
            junk_items[item] += value
        
