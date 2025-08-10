energy_points = int(input())
won_battles_count = 0
energy_per_distance = 1

while energy_points >= 0:

    curr_distance_to_ennemy = input()

    if curr_distance_to_ennemy == "End of battle":
        print(f"Won battles: {won_battles_count}. Energy left: {energy_points}")
        break
    
    energy_points_needed = int(curr_distance_to_ennemy) * energy_per_distance



    if energy_points < energy_points_needed:
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy_points} energy")
        break

    energy_points -= energy_points_needed
    won_battles_count += 1
    
    if not won_battles_count % 3:
        energy_points += won_battles_count

