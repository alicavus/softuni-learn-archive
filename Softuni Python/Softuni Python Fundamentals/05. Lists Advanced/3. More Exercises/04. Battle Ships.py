ships_matrix_count = int(input())

ships_matrix = [[]] * ships_matrix_count

destroyed_ships = 0

for row_idx in range(ships_matrix_count):
    row = [int(x) for x in input().split()]
    ships_matrix[row_idx] = row

attack_fights = [[int(x) for x in y.split("-")] for y in input().split()]

for attack_fight in attack_fights:
    row_idx, col_idx = attack_fight
    if ships_matrix[row_idx][col_idx]:
        ships_matrix[row_idx][col_idx] -= 1
        if not ships_matrix[row_idx][col_idx]:
            destroyed_ships += 1


print(destroyed_ships)