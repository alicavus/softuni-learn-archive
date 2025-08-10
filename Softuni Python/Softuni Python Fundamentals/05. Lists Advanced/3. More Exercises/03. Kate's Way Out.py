def can_move(kate_pos: list[int, int], cell: list[int, int]) -> bool:
    global maze
    if (kate_pos[1] == cell[1] and kate_pos[0] in [cell[0]-1, cell[0]+1])\
          or (kate_pos[0] == cell[0] and kate_pos[1] in [cell[1]-1, cell[1]+1]):
        if maze[cell[0]][cell[1]] == ' ':
            return True
    return False

rows_count = int(input())

maze = [[]] * rows_count

kate_pos = []

visited = []

for row_idx in range(rows_count):
    maze[row_idx] = [x for x in input()]
    if maze[row_idx].count("k"):
        kate_pos = [row_idx, maze[row_idx].index("k")]



print(kate_pos, "\n", maze)
    


