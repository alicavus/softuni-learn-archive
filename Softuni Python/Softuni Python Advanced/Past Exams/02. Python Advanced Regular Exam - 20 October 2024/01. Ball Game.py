from collections import deque

strengths = [int(x) for x in input().split()]
accuracies = deque([int(x) for x in input().split()])

goals = 0

while strengths and accuracies:
    strength = strengths[-1]
    accuracy = accuracies[0]

    kick_sum = accuracy + strength

    if kick_sum == 100:
        accuracies.popleft()
        strengths.pop()
        goals += 1

    elif kick_sum < 100:
        if accuracy > strength:
            strengths.pop()
        elif accuracy < strength:
            accuracies.popleft()
        else:
            strengths[-1] = kick_sum
            accuracies.popleft()
    else:
        strengths[-1] -= 10
        accuracies.append(accuracies.popleft())

if not goals:
    print("Paul failed to score a single goal.")

elif goals < 3:
    print(f"Paul failed to make a hat-trick.\nGoals scored: {goals}")

elif goals == 3:
    print(f"Paul scored a hat-trick!\nGoals scored: {goals}")

else:
    print(f"Paul performed remarkably well!\nGoals scored: {goals}")

if strengths:
    print("Strength values left: ", end="")
    print(*strengths, sep=", ")

if accuracies:
    print("Accuracies left: ", end="")
    print(*accuracies, sep=", ")