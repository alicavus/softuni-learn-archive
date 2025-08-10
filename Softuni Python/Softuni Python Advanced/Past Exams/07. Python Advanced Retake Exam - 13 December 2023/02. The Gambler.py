board_size = int(input())
board = []

GAMBLER_CHAR = 'G'
EMPTY_CHAR = '-'
WIN_CHAR = 'W'
PENALTY_CHAR = 'P'
JACKPOT_CHAR = 'J'
END_COMMAND = 'end'
WIN_AMOUNT = 100
JACKPOT_AMOUNT = 100_000
PENALTY_AMOUNT = 200
INITIAL_AMOUNT = 100

win_amount = INITIAL_AMOUNT
has_jackpot = False

gambler_pos = [-1, -1]
jackpots = []
wins = []
penalties = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for ridx in range(board_size):
    row = list(input())
    for cidx in range(board_size):
        cur_pos = [ridx, cidx]
        if row[cidx] == GAMBLER_CHAR:
            gambler_pos = cur_pos
        elif row[cidx] == WIN_CHAR:
            wins += [cur_pos]
        elif row[cidx] == PENALTY_CHAR:
            penalties += [cur_pos]
        elif row[cidx] == JACKPOT_CHAR:
            jackpots += [cur_pos]
    board.append(row)

while win_amount > 0 and not has_jackpot:
    try:
        direction_ridx, direction_cidx = directions[input()]
    except KeyError:
        break
    else:
        new_gambler_ridx = gambler_pos[0] + direction_ridx
        new_gambler_cidx = gambler_pos[1] + direction_cidx
        new_gambler_pos = [new_gambler_ridx, new_gambler_cidx]


    if any([pos not in range(board_size) for pos in new_gambler_pos]):
        win_amount = 0

    elif new_gambler_pos in wins:
        win_amount += WIN_AMOUNT
        wins.remove(new_gambler_pos)

    elif new_gambler_pos in jackpots:
        win_amount += JACKPOT_AMOUNT
        has_jackpot = True
        jackpots.remove(new_gambler_pos)

    elif new_gambler_pos in penalties:
        win_amount -= PENALTY_AMOUNT
        penalties.remove(new_gambler_pos)

    board[gambler_pos[0]][gambler_pos[1]] = EMPTY_CHAR
    gambler_pos = new_gambler_pos
    board[gambler_pos[0]][gambler_pos[1]] = GAMBLER_CHAR

if has_jackpot:
    print(f"You win the Jackpot!\nEnd of the game. Total amount: {win_amount}$")
elif win_amount > 0:
    print(f"End of the game. Total amount: {win_amount}$")
else:
    print(f"Game over! You lost everything!")

if win_amount > 0:
    for row in board:
        print(''.join(row))