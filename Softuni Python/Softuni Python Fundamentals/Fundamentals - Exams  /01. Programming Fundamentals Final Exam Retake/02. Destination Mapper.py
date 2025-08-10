def is_valid_location(location: str) -> bool:
    return len(location) >= 3 and location.isalpha() and location[0].isupper()


locations = input()

destinations = []

prev_delim = None

cur_location = ""

for c in locations:
    if c in "=/":
        cur_delim = c
        if cur_delim == prev_delim:
            if is_valid_location(cur_location):
                destinations.append(cur_location)
        cur_location = ""
        prev_delim = cur_delim
        continue
    cur_location += c

print(f"""Destinations: {", ".join(destinations)}
Travel Points: {sum([len(x) for x in destinations])}""")