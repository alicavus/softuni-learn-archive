def sumfinder(*args):
    positives = [arg for arg in args if arg > 0]
    negatives = [arg for arg in args if arg < 0]
    sum_negatives = sum(negatives if negatives else [0])
    sum_positives = sum(positives if positives else [0])

    stronger, weaker = ("negatives", "positives") if abs(sum_negatives) > sum_positives else ("positives", "negatives")

    return f"{sum_negatives}\n{sum_positives}\nThe {stronger} are stronger than the {weaker}"

print(sumfinder(*[int(x) for x in input().split()]))