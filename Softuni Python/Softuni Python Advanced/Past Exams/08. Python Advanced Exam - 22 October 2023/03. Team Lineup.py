def team_lineup(*args: list[tuple[str, str]]) -> str:
    players = { }
    for player_data in args:
        player_name, player_country = player_data

        if player_country not in players:
            players[player_country] = []
        players[player_country] += [player_name]

    result = []

    for country_stats in sorted(players.items(), key=lambda item: (-len(item[1]),item[0])):
        result += [f"{country_stats[0]}:"]
        for player_name in country_stats[1]:
            result += [f"  -{player_name}"]

    return "\n".join(result)

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print('----')

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print('----')


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

