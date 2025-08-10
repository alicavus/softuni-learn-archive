# The difference with Judge is caused by ordering of output list

def is_valid_location(location: str) -> bool:
    return len(location) >= 3 and location.isalpha() and location[0].isupper()

locations = input()

destinations = []

eq_indices = []
sl_indices = []

eq_ix = 0
sl_ix = 0

while locations.find("=", eq_ix) > -1:
    ix = locations.find("=", eq_ix)
    eq_indices.append(ix)
    eq_ix = ix + 1

while locations.find("/", sl_ix) > -1:
    ix = locations.find("/", sl_ix)
    sl_indices.append(ix)
    sl_ix = ix + 1

for ix in range(len(eq_indices)-1):
    location = locations[eq_indices[ix]+1:eq_indices[ix+1]]
    if is_valid_location(location):
        destinations.append(location)

for ix in range(len(sl_indices)-1):
    location = locations[sl_indices[ix]+1:sl_indices[ix+1]]
    if is_valid_location(location):
        destinations.append(location)

print(eq_indices, sl_indices)

print(f"""Destinations: {", ".join(destinations)}
Travel Points: {sum([len(x) for x in destinations])}""")
