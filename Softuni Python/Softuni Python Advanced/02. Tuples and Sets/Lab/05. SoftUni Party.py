number_of_guests = int(input())

guests = set()

for _ in "*" * number_of_guests:
    guests.add(input())

while True:
    guest = input()

    if guest.lower() == "end":
        break

    if guest in guests:
        guests.remove(guest)

print(len(guests))
for guest in sorted(guests):
    print(guest)