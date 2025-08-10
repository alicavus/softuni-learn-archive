treasure_chest = input().split("|")

while True:
    cmd = input()

    if cmd == "Yohoho!":
        break

    cmd_list = cmd.split(" ")

    match cmd_list[0]:
        case "Loot":
            for item in cmd_list[1:]:
                if item in treasure_chest:
                    continue
                treasure_chest = [item] + treasure_chest
        case "Drop":
            idx = int(cmd_list[1])
            if not 0 <= idx < len(treasure_chest):
                continue
            item = treasure_chest.pop(idx)
            treasure_chest.append(item)
        case "Steal":
            cnt_items = int(cmd_list[1])
            if not 0 < cnt_items:
                continue
            items = treasure_chest[-cnt_items:]
            treasure_chest = treasure_chest[:len(treasure_chest) - cnt_items] if cnt_items < len(treasure_chest) else []
            print(", ".join(items))
    
if treasure_chest:
    avg_gain = sum([len(x) for x in treasure_chest]) / len(treasure_chest)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")