count_of_coffees = 0
while True:
    activity = input()
    if activity == "END":
        break
    if activity.lower() in ("coding", "dog", "cat", "movie"):
        if activity.islower():
            count_of_coffees += 1
        elif activity.isupper():
            count_of_coffees += 2

print("You need extra sleep" if count_of_coffees > 5 else f"{count_of_coffees}")
