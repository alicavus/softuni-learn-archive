def accommodate(*args, **kwargs):
    accommodated = {}
    count_unaccommodated = 0

    for curr_guest_cnt in args:
        has_accommodated = False
        for room_data in sorted(kwargs.items(), key=lambda item: (item[1], item[0])):
            room_name, room_capacity = room_data
            if room_capacity >= curr_guest_cnt:
                has_accommodated = True
                accommodated[room_name] = curr_guest_cnt
                del kwargs[room_name]
                break
        if not has_accommodated:
            count_unaccommodated += curr_guest_cnt

    result = []

    if accommodated:
        result += [f"A total of {len(accommodated)} accommodations were completed!"]
        for room_data in sorted(accommodated.items(), key=lambda item: item[0]):
            room_name, room_guest_cnt = room_data
            result += [f"<Room {room_name.split('_')[1]} accommodates {room_guest_cnt} guests>"]
    else:
        result += [f"No accommodations were completed!"]

    if count_unaccommodated:
        result +=  [f"Guests with no accommodation: {count_unaccommodated}"]

    if kwargs:
        result += [f"Empty rooms: {len(kwargs)}"]

    return "\n".join(result)

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
