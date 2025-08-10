def is_valid(place: str) -> bool:
    return place.isalpha() and place[0].isupper() and len(place) >= 3

places_string = input()

destinations = []

prev_delim = None

cur_place = ""
for c in places_string:
    if c in "=/":
        if c == prev_delim:
            if is_valid(place=cur_place):
                destinations.append(cur_place)
        prev_delim = c
        cur_place = ""
    else:
        cur_place += c

travel_points = sum([len(x) for x in destinations])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
