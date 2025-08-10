pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

stalemate = True

while True:
    cmd = input()

    if cmd == "Retire":
        break

    cmd_list = cmd.split(" ")

    match cmd_list[0]:
        case "Fire":
            idx = int(cmd_list[1])
            damage = int(cmd_list[2])

            if not 0 <= idx < len(warship):
                continue

            if warship[idx] <= damage:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break

            warship[idx] -= damage
        
        case "Defend":
            start_idx = int(cmd_list[1])
            end_idx = int(cmd_list[2])
            damage = int(cmd_list[3])

            if not 0 <= start_idx <= end_idx < len(pirate_ship):
                continue

            for idx in range(start_idx, end_idx+1):
                if pirate_ship[idx] <= damage:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
                pirate_ship[idx] -= damage
            
        case "Repair":
            idx = int(cmd_list[1])
            health = int(cmd_list[2])

            if not 0 <= idx < len(pirate_ship):
                continue

            if max_health <= pirate_ship[idx] + health:
                pirate_ship[idx] = max_health
            
            else:
                pirate_ship[idx] += health
        
        case "Status":
            need_repair = len([x for x in pirate_ship if x < 0.2 * max_health])

            print(f"{need_repair} sections need repair.")

if stalemate:
    print(f"""Pirate ship status: {sum(pirate_ship)}
Warship status: {sum(warship)}""")






