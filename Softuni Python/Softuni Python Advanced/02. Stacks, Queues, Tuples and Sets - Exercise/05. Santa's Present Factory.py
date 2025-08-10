from collections import deque

materials = [int(mat) for mat in input().split()]
magic = deque([int(mag) for mag in input().split()])

presents = {150 : "Doll", 250 : "Wooden train", 300 : "Teddy bear", 400 : "Bicycle"}
crafted = {}

while materials and magic:
    curr_material = materials[-1]
    curr_magic = magic[0]

    while curr_material == 0 and materials:
        materials.pop()
        if materials:
            curr_material = materials[-1]
    
    while curr_magic == 0 and magic:
        magic.popleft()
        if magic:
            curr_magic = magic[0]

    curr_multiplication_magic = curr_magic * curr_material

    if curr_multiplication_magic == 0:
        break

    elif curr_multiplication_magic in presents:
        curr_present = presents[curr_multiplication_magic]
        if curr_present not in crafted:
            crafted[curr_present] = 0
        crafted[curr_present] += 1

        materials.pop()
        magic.popleft()
    
    elif curr_multiplication_magic < 0:
        materials.pop()
        materials.append(curr_magic + curr_material)
        magic.popleft()
    
    else:
        magic.popleft()
        materials[-1] += 15

if all(x in crafted for x in ("Doll", "Wooden train")) or \
    all(x in crafted for x in ("Bicycle", "Teddy bear")):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    left_materials = [f"{x}" for x in reversed(materials)]
    print("Materials left:", ", ".join(left_materials))

elif magic:
    left_magic = [f"{x}" for x in magic]
    print("Magic left:", ", ".join(left_magic))

for crafted_present in sorted(crafted.keys()):
    print(f"{crafted_present}: {crafted[crafted_present]}")