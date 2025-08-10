from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

colors_data = deque(input().split())


colors = []

while colors_data:
    if len(colors_data) > 1:
        curr_color_data = (colors_data.popleft(), colors_data.pop())
    else:
        curr_color_data = (colors_data.pop(),"")
    
    found_color = None
    
    if curr_color_data[0] + curr_color_data[1] in main_colors.union(secondary_colors):
        found_color = curr_color_data[0] + curr_color_data[1]

    elif curr_color_data[1] + curr_color_data[0] in main_colors.union(secondary_colors):
        found_color = curr_color_data[1] + curr_color_data[0]
    
    if found_color is None:
        curr_color_data = tuple([x[:-1] for x in curr_color_data if x[:-1] != ""])

        colors_data_len = len(colors_data)

        if(colors_data_len % 2): colors_data_len -= 1
        
        colors_data_len //= 2
        
        new_colors_data = list(colors_data)[:colors_data_len]

        for _color_data in curr_color_data:
            new_colors_data.append(_color_data)
        
        new_colors_data += list(colors_data)[colors_data_len:]

        colors_data = deque(new_colors_data)

    else:
        colors.append(found_color)

for color in colors:
    if color in secondary_colors:
        if color == "orange":
            if "red" not in colors or "yellow" not in colors:
                colors.remove(color)
        elif color == "purple":
            if "red" not in colors or "blue" not in colors:
                colors.remove(color)
        elif color == "green":
            if "yellow" not in colors or "blue" not in colors:
                colors.remove(color)

print(colors)



    

    
    

