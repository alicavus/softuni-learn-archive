def sort_games(*registrations, **release_ids) -> str:
    def get_date(date: str) -> str:
        return "_".join(date.split("_")[:-1])

    console_games = {}
    pc_games = {}

    for game_data in registrations:
        game_type, game_title = game_data

        if game_type == "console":
            tg = console_games
        
        elif game_type == "pc":
            tg = pc_games
        
        for rel_data in release_ids.items():
            if rel_data[1] == game_title:
                tg[rel_data[0]] = game_title
    
    result = []
    
    for tg in [console_games, pc_games]:
        if tg:
            result += [f"{'Console' if tg == console_games else 'PC'} Games:"]
            for rel_data in sorted(tg.items(), key=lambda item: item[0], reverse=(tg == pc_games)):
                result += [f"{'<<<' if tg == pc_games else '>>>'}{get_date(rel_data[0])}: {rel_data[1]}"]
    
    return "\n".join(result)

print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))

print("------")

print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))

print("------")


print(sort_games(
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("console", "Blade Echo"),
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
))

print("------")


print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))


