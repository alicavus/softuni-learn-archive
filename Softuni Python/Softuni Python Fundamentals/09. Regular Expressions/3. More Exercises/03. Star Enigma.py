from re import search, findall, IGNORECASE

planets = {
    "Attacked": [],
    "Destroyed": []
}

for _ in range(int(input())):
    message = input()
    remove_count_ascii = len(findall(pattern=r'[star]', string=message, flags=IGNORECASE))

    decrypted_message = "".join([chr(ord(char) - remove_count_ascii) for char in message])

    planet_name_match = search(pattern=r'@[A-Za-z]+', string=decrypted_message)
    planet_population_match = search(pattern=r'\:\d+', string=decrypted_message)
    attack_type_match = search(pattern=r'!A!|!D!', string=decrypted_message)
    soldier_count_match = search(pattern=r'->\d+', string=decrypted_message)

    if None in [planet_name_match, planet_population_match, attack_type_match, soldier_count_match]:
        continue

    planet_name = planet_name_match.group(0)
    attack_type = attack_type_match.group(0)


    if attack_type == "!A!":
        planets['Attacked'].append(planet_name[1:])
    
    elif attack_type == "!D!":
        planets['Destroyed'].append(planet_name[1:])
    
for attack_type in ("Attacked", "Destroyed",):
    print(f"{attack_type} planets: {len(planets[attack_type])}")
    for planet_name in sorted(planets[attack_type], key=lambda item: item):
        print(f"-> {planet_name}")