size = int(input())

knights = []

knight_moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for ridx in range(size):
    row = input()
    idx = 0
    while True:
        idx = row.find("K", idx)
        if idx > -1:
            knights.append([ridx, idx])
            idx += 1
        else:
            break

knights_attack_count = [1] * len(knights)

removed_knights = []

while sum(knights_attack_count):
    for knidx in range(len(knights)):
        cur_cnt = 0
        cur_knight = knights[knidx]
        for knight_move in knight_moves:
            attack_field_ridx, attack_field_cidx = cur_knight[0] + knight_move[0], cur_knight[1] + knight_move[1]
            if attack_field_ridx not in range(size) or attack_field_cidx not in range(size):
                continue
            if [attack_field_ridx, attack_field_cidx] in knights:
                cur_cnt += 1
        knights_attack_count[knidx] = cur_cnt

    max_attack_cnt = max(knights_attack_count) if knights_attack_count else 0

    if max_attack_cnt:
        idx_to_remove = knights_attack_count.index(max_attack_cnt)

        removed_knights.append(knights.pop(idx_to_remove))
        knights_attack_count.pop(idx_to_remove)

print(len(removed_knights))
            

