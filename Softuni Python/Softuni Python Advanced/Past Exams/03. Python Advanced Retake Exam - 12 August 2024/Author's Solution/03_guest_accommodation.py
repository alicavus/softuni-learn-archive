def accommodate(*guest_groups, **available_rooms):
    accommodations = {}
    unaccommodated_guests = 0

    # Order the available rooms by capacity and room number
    rooms = sorted(available_rooms.items(), key=lambda r: (r[1], r[0]))

    for guests in guest_groups:
        is_accommodated = False

        for room_key, capacity in rooms:  # Iterating over sorted available rooms ensures finding the best match
            if capacity >= guests:
                room_number = room_key.split('_')[1]
                if room_number not in accommodations:
                    accommodations[room_number] = guests
                    # Remove the occupied room and break the loop
                    rooms.remove((room_key, capacity))
                    is_accommodated = True
                    break
        if not is_accommodated:
            unaccommodated_guests += guests

    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_number in sorted(accommodations.keys()):
            result.append(f"<Room {room_number} accommodates {accommodations[room_number]} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result).strip()


# Example usage
# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
# print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
