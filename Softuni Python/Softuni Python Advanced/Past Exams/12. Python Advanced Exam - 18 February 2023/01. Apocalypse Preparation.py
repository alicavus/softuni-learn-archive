from collections import deque, defaultdict

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

resources_needed = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}

collected_items = {res:0 for res in resources_needed.values()}

while textiles and medicaments:
    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()
    curr_sum = curr_textile + curr_medicament

    if curr_sum in resources_needed:
        collected_items[resources_needed[curr_sum]] += 1
    elif curr_sum > max(resources_needed.keys()):
        collected_items[resources_needed[max(resources_needed.keys())]] += 1
        curr_sum -= max(resources_needed.keys())
        medicaments[-1] += curr_sum
    else:
        medicaments.append(curr_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif textiles:
    print("Medicaments are empty.")
else:
    print("Textiles are empty.")

for item_data in filter(lambda item: item[1] > 0, sorted(collected_items.items(), key=lambda item:(-item[1], item[0]))):
    print(f"{item_data[0]} - {item_data[1]}")

if medicaments:
    print("Medicaments left:", ", ".join(map(str, reversed(medicaments))))

elif textiles:
    print("Textiles left:", ", ".join(map(str, textiles)))


