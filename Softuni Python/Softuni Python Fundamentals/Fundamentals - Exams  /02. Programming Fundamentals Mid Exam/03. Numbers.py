
sequence = [int(x) for x in input().strip().split(" ")]

avg = sum(sequence) / len(sequence)

above_avg = [x for x in sequence if avg < x]

above_avg.sort(reverse=True)

print("No" if above_avg == [] else " ".join([str(x) for x in above_avg[:5]]))



