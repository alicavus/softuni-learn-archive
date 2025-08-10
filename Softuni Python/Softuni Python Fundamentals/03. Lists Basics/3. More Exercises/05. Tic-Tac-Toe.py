def winner(field: list) -> str:
    if any([l in [['1'], ['2']] for l in [list(set([field[0][0], field[1][1], field[2][2]])), list(set([field[0][2], field[1][1], field[2][0]]))]]):
        return field[1][1]
    
    for row_idx in range(3):
        if list(set([field[row_idx][x] for x in range(3)])) in [['1'], ['2']]:
            return field[row_idx][0]
    
    for col_idx in range(3):
        if list(set([field[x][col_idx] for x in range(3)])) in [['1'], ['2']]:
            return field[0][col_idx]
    
    return ''


field = [[]] * 3

for idx in [0, 1, 2]:
    field[idx] = input().strip().split(' ')

winner_player = winner(field)

if winner_player and winner_player in '12':
    print('First player won' if winner_player == '1' else 'Second player won')
else:
    print('Draw!')
