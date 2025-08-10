# Read the sequences of worms and holes as lists of integers.
worms = list(map(int, input().split()))
holes = list(map(int, input().split()))

# Initialize variables to keep track of matches and the original number of worms.
matches = 0
worms_size = len(worms)

# While there are still worms and holes to process.
while worms and holes:
    # Get the current worm and hole for comparison.
    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        # A match is found, remove both the worm and the hole.
        worms.pop()
        holes.pop(0)
        matches += 1
    else:
        # Decrease the worm size by 3 and check if it becomes zero or negative.
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
        holes.pop(0)


# If there are matches, print the number of matches.
print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != worms_size:
    # If not all worms found a suitable hole, print the remaining worms.
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    # If all worms found suitable holes, print a message.
    print("Every worm found a suitable hole!")

# Print the remaining holes, if any.
print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")
