clothes = list(map(int, input().split()))
rack_capacity = int(input())

racks = []
cur_rack = 0

while clothes:
    cur_clothes = clothes[-1]

    if cur_rack + cur_clothes > rack_capacity:

        racks.append(cur_rack)
        cur_rack = 0
    
    cur_rack += cur_clothes
    
    clothes.pop()


if cur_rack:
    racks.append(cur_rack)

print(len(racks))
