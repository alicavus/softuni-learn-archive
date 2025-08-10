players = {}

def fight(player_one: str, player_two: str) -> None:
    global players
    if player_one not in players.keys() or player_two not in players.keys():
        return
    if all(skill not in players[player_two].keys() for skill in players[player_one].keys()):
        return
    
    player_one_total_skill = sum(players[player_one].values())
    player_two_total_skill = sum(players[player_two].values())

    if player_one_total_skill > player_two_total_skill:
        players.pop(player_two)
    elif player_one_total_skill < player_two_total_skill:
        players.pop(player_one)

def print_players() -> None:
    global players

    players_sorted = dict(sorted(players.items(), key=lambda item: [-sum(item[1].values()), item[0]]))

    for player in players_sorted.keys():
        print(f"{player}: {sum(players_sorted[player].values())} skill")
        player_sorted_by_skill = dict(sorted(players_sorted[player].items(), key=lambda item:[-item[1], item[0]]))
        for skill, points in player_sorted_by_skill.items():
            print(f"- {skill} <::> {points}")


while True:
    input_line = input()

    if input_line == "Season end":
        print_players()
        break

    if " -> " in input_line:
        player, position, skill = input_line.split(" -> ")
        if player not in players.keys():
            players[player] = {position: int(skill)}
        else:
            if position not in players[player].keys():
                players[player][position] = int(skill)
            else:
                players[player][position] = max(players[player][position], int(skill))
        
    elif " vs " in input_line:
        player_one, player_two = input_line.split(" vs ")
        
        fight(player_one, player_two)


