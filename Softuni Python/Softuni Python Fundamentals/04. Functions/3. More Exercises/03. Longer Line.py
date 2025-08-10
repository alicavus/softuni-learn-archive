
def closest_to_center(p1: list[float, float], p2: list[float, float]) -> list[float, float]:
    d1 = (p1[0] ** 2 + p1[1] ** 2) ** 0.5
    d2 = (p2[0] ** 2 + p2[1] ** 2) ** 0.5

    return p1 if d1 <= d2 else p2

def line_length(p1: list[float, float], p2: list[float, float]) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def pretty_line_coordinates(p1: list[float, float], p2: list[float, float]) -> list[list[int, int], list[int, int]]:
    if closest_to_center(p1, p2) == p1:
        return [[int(x) for x in p1], [int(x) for x in p2]]
    else:
        return [[int(x) for x in p2], [int(x) for x in p1]]

def longer_line(l1: list[list[float, float], list[float, float]], l2: list[list[float, float], list[float, float]]) -> list[list[int, int], list[int, int]]:
    line_one_len = line_length(p1=l1[0], p2=l1[1])
    line_two_len = line_length(p1=l2[0], p2=l2[1])

    if line_one_len >= line_two_len:
        return pretty_line_coordinates(l1[0], l1[1])
    
    else:
        return pretty_line_coordinates(l2[0], l2[1])

coordinates = [float(input()) for _ in range(8)]

line = longer_line(l1=[coordinates[:2], coordinates[2:4]], l2=[coordinates[4:6], coordinates[6:]])

print(f"({line[0][0]}, {line[0][1]})({line[1][0]}, {line[1][1]})")