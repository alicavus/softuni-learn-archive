while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    school = "Gryffindor" if len(name) < 5 else "Slytherin" if len(name) == 5 else "Ravenclaw" if len(name) == 6 else "Hufflepuff"
    print(f"{name} goes to {school}.")
