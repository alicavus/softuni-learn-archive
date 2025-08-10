red_cards_count = {
    "team a": [False] * 11,
    "team b": [False] * 11
}

red_cards = input().strip().split(' ')

is_match_terminated = False

for red_card in red_cards:
    player_team = red_card.split("-")[0]
    player_index = int(red_card.split("-")[1])
    player_index -= 1

    dict_key = "team a" if player_team == 'A' else "team b" if player_team == 'B' else ""

    if dict_key in red_cards_count and player_index in range(11):
        red_cards_count[dict_key][player_index] = True
        
        if red_cards_count["team a"].count(True) == 5 \
            or red_cards_count["team b"].count(True) == 5:
            is_match_terminated = True
            break

print(f"Team A - {red_cards_count['team a'].count(False)}; Team B - {red_cards_count['team b'].count(False)}")

if is_match_terminated:
    print("Game was terminated")