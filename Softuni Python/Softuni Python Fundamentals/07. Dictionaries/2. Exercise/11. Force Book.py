force_sides = {}
users = {}

while True:
    force_info = input()

    if force_info == "Lumpawaroo":
        for force_side in force_sides:
            if len(force_sides[force_side]):
                print(f"Side: {force_side}, Members: {len(force_sides[force_side])}")
                print("\n".join([f'! {force_user}' for force_user in force_sides[force_side]]))
        break

    if " | " in force_info:
        force_side, force_user = force_info.split(" | ")

        if force_side not in force_sides and force_user not in users:
            force_sides[force_side] = [force_user]
            users[force_user] = force_side
        
        elif force_user not in users:
            force_sides[force_side] += [force_user]
            users[force_user] = force_side

    elif " -> " in force_info:
        force_user , force_side = force_info.split(" -> ")

        if force_side not in force_sides and force_user not in users:
            force_sides[force_side] = [force_user]
            users[force_user] = force_side

        elif force_side not in force_sides:
            force_sides[users[force_user]].remove(force_user)
            force_sides[force_side] = [force_user]
            users[force_user] = force_side

        elif force_user not in users:
            force_sides[force_side] += [force_user]
            users[force_user] = force_side
        

        elif force_side in force_sides and force_user in users:
            force_sides[users[force_user]].remove(force_user)
            force_sides[force_side] += [force_user]
            users[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")




