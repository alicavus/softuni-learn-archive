neighborhood_rows, neighborhood_columns = map(int, input().split())

delivery_boy_ridx, delivery_boy_cidx = -1, -1
delivery_boy_start_ridx, delivery_boy_start_cidx = -1, -1
delivery_address_ridx, delivery_address_cidx = -1, -1
restaurant_ridx, restaurant_cidx = -1, -1
obstacles = []
neighborhood = []

DELIVERY_BOY_CHAR = 'B'
DELIVERY_ADDRESS_CHAR = 'A'
OBSTACLE_CHAR = '*'
ROAD_CHAR = '-'
RESTAURANT_WITH_PIZZA_CHAR = 'P'
RESTAURANT_WITHOUT_PIZZA__CHAR = 'R'
PIZZA_CHAR = 'P'
WALKED_CHAR = '.'
EMPTY_CHAR = ' '

has_collected, has_failed, has_delivered = False, False, False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(neighborhood_rows):
    row = list(input())
    for cidx in range(neighborhood_columns):
        if row[cidx] == DELIVERY_BOY_CHAR:
            delivery_boy_ridx, delivery_boy_cidx = ridx, cidx
            delivery_boy_start_cidx, delivery_boy_start_ridx = cidx, ridx
        elif row[cidx] == DELIVERY_ADDRESS_CHAR:
            delivery_address_ridx, delivery_address_cidx = ridx, cidx
        elif row[cidx] == OBSTACLE_CHAR:
            obstacles += [[ridx, cidx]]
        elif row[cidx] == RESTAURANT_WITH_PIZZA_CHAR:
            restaurant_ridx, restaurant_cidx = ridx, cidx

    neighborhood.append(row)

while not has_failed and not has_delivered:
    direction_ridx, direction_cidx = directions[input()]
    new_delivery_boy_ridx = delivery_boy_ridx + direction_ridx
    new_delivery_boy_cidx = delivery_boy_cidx + direction_cidx

    if not 0 <= new_delivery_boy_ridx < neighborhood_rows \
        or not 0 <= new_delivery_boy_cidx < neighborhood_columns:
        has_failed = True
        print("The delivery is late. Order is canceled.")

    new_delivery_boy_pos = [new_delivery_boy_ridx, new_delivery_boy_cidx]

    if new_delivery_boy_pos in obstacles:
        continue

    elif new_delivery_boy_pos == [restaurant_ridx, restaurant_cidx]:
        if not has_collected:
            print("Pizza is collected. 10 minutes for delivery.")
        has_collected = True
        neighborhood[restaurant_ridx][restaurant_cidx] = RESTAURANT_WITHOUT_PIZZA__CHAR

    elif new_delivery_boy_pos == [delivery_address_ridx, delivery_address_cidx]:
        if has_collected:
            print("Pizza is delivered on time! Next order...")
            has_delivered = True
            neighborhood[delivery_address_ridx][delivery_address_cidx] = PIZZA_CHAR

    if not has_failed:
        if neighborhood[new_delivery_boy_ridx][new_delivery_boy_cidx] == ROAD_CHAR:
            neighborhood[new_delivery_boy_ridx][new_delivery_boy_cidx] = WALKED_CHAR
        delivery_boy_ridx, delivery_boy_cidx = new_delivery_boy_ridx, new_delivery_boy_cidx

neighborhood[delivery_boy_start_ridx][delivery_boy_start_cidx] = DELIVERY_BOY_CHAR if has_delivered else EMPTY_CHAR

for row in neighborhood:
    print(*row, sep='')