my_sheeps = list(reversed(input().split(", ")))

wolf_index = my_sheeps.index("wolf")
print("Please go away and stop eating my sheep" if not(wolf_index) else f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")