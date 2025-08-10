from collections import deque
food_supplies = [int(x) for x in input().split(", ")]
stamina_supplies = deque(map(int, input().split(", ")))

peaks = {
    80: {"name": "Vihren", "status": False},
    90: {"name": "Kutelo", "status": False},
    100: {"name": "Banski Suhodol", "status": False},
    60: {"name": "Polezhan", "status": False},
    70: {"name": "Kamenitza", "status": False}
}

DAYS = 7

for daynum in range(DAYS):
    if len(list(filter(lambda x: x[1]["status"], peaks.items()))) == len(peaks):
        break
    if not food_supplies or not stamina_supplies:
        break

    curr_food = food_supplies.pop()
    curr_stamina = stamina_supplies.popleft()

    curr_supplies = curr_food + curr_stamina

    for peak_data in peaks.items():
        if peak_data[1]["status"]:
            continue
        elif not peak_data[1]["status"]:
            if curr_supplies >= peak_data[0]:
                peaks[peak_data[0]]["status"] = True
            break

conquered_peaks = list(filter(lambda x: x[1]["status"], peaks.items()))

if len(conquered_peaks) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak_data in conquered_peaks:
        print(peak_data[1]["name"])