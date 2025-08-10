sequence_of_integers = [int(x) for x in input().split()]

total_pokemons_value = 0

while sequence_of_integers:
    idx = int(input())

    if idx < 0:
        idx = 0
        if len(sequence_of_integers) > 1:
            sequence_of_integers = [sequence_of_integers[0], sequence_of_integers[-1]] + sequence_of_integers[1:]
    
    elif idx >= len(sequence_of_integers):
        idx = -1
        if len(sequence_of_integers) > 1:
            sequence_of_integers = sequence_of_integers[:-1] + [sequence_of_integers[0], sequence_of_integers[-1]]
    
    catch_pokemon_value = sequence_of_integers.pop(idx)

    for curr_pokemon_left_idx in range(len(sequence_of_integers)):
        if sequence_of_integers[curr_pokemon_left_idx] <= catch_pokemon_value:
            sequence_of_integers[curr_pokemon_left_idx] += catch_pokemon_value
        else:
            sequence_of_integers[curr_pokemon_left_idx] -= catch_pokemon_value
    total_pokemons_value += catch_pokemon_value

print(total_pokemons_value)
    
