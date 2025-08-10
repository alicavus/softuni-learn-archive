from collections import deque

def complete_circle(pumps_conf: list) -> bool:
    fuel = 0
    for cur_station in pumps_conf:
        fuel += cur_station[0]
        if fuel < cur_station[1]:
            return False
        fuel -= cur_station[1]
    
    return True

fuel = 0

pumps_count = int(input())
pumps = [[0, 0]] * pumps_count

for idx in range(pumps_count):
    pumps[idx] = list(map(int, input().split()))


cur_idx = 0

while not complete_circle(pumps[cur_idx:] + pumps[:cur_idx]):
    cur_idx += 1

    if cur_idx >= len(pumps):
        raise ValueError

print(cur_idx)



