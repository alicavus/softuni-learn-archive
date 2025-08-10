from collections import deque

strengths = [int(element) for element in input().split(' ')]
accuracies = deque([int(element) for element in input().split(' ')])

total_goals = 0

while strengths and accuracies:
    current_strength = strengths[-1]  # Last element in the strengths list (stack behavior)
    current_accuracy = accuracies[0]  # First element in the accuracies deque (queue behavior)
    sum_values = current_strength + current_accuracy

    if sum_values == 100:
        # Goal: Remove both the strength and accuracy
        strengths.pop()
        accuracies.popleft()
        total_goals += 1

    elif sum_values < 100:
        if current_strength < current_accuracy:
            strengths.pop()
        elif current_strength > current_accuracy:
            accuracies.popleft()
        else:
            strengths[-1] = current_strength + current_accuracy
            accuracies.popleft()

    else:  # sum_values > 100
        strengths[-1] -= 10
        accuracies.append(accuracies.popleft())

# Output results based on the number of goals scored
if total_goals == 3:
    print("Paul scored a hat-trick!")
elif total_goals > 3:
    print("Paul performed remarkably well!")
elif total_goals == 0:
    print("Paul failed to score a single goal.")
else:
    print("Paul failed to make a hat-trick.")

if total_goals > 0:
    print(f"Goals scored: {total_goals}")

if strengths:
    print("Strength values left:", ", ".join(map(str, strengths)))
if accuracies:
    print("Accuracy values left:", ", ".join(map(str, accuracies)))
