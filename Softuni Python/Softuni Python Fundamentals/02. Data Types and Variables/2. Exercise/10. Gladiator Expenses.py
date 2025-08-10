lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_count = lost_fights // 2
swords_count = lost_fights // 3
shield_count = lost_fights // 6
armor_count = lost_fights // 12

total_expences = helmet_price * helmets_count + sword_price * swords_count
total_expences += shield_price * shield_count + armor_price * armor_count

print(f"Gladiator expenses: {total_expences:.2f} aureus")