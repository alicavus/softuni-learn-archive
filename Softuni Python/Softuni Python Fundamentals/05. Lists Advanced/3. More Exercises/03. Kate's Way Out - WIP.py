def spaces_finder(maze: list[list[str]]) -> dict:
    spaces = []
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == ' ':
                spaces += [[row_idx, col_idx]]
    
    exits = spaces_on_edges(spaces)
    corridors = [x for x in spaces if x not in exits]
    return {"corridors": corridors, "exits": exits}

def spaces_on_edges(spaces: list[list[int, int]]) -> list[list]:
    global maze
    spaces_list = []
    for space in spaces:
        if space != []:
            if space[0] in [0, len(maze)-1] or space[1] in [0, len(maze[0]) -1]:
                spaces_list += [space]
    return spaces_list


number_of_rows = int(input())

maze = [[]] * number_of_rows

kate_pos = []

for row_idx in range(number_of_rows):
    maze[row_idx] = [c for c in input()]

    if "k" in maze[row_idx]:
        kate_pos = [row_idx, maze[row_idx].index("k")]

maze_dict = spaces_finder(maze=maze)

ways_out = []

for door in maze_dict["exits"]:
    dor_row_idx, dor_col_idx = door
    way = [door]

    corridors = maze_dict["corridors"]
    
    for corridor in corridors:
        cor_row_idx, cor_col_idx = corridor
        if (cor_row_idx == dor_row_idx and cor_col_idx in [dor_col_idx-1, dor_col_idx+1]) or \
        cor_col_idx == dor_col_idx and cor_row_idx in [dor_row_idx-1, dor_row_idx+1]:
            way += [corridor]
            dor_row_idx, dor_col_idx = corridor
    ways_out += [way]


print(ways_out)


