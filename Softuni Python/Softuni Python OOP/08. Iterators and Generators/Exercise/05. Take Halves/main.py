def solution():

    def integers():
        cur = 1
        while True:
            yield cur
            cur += 1

    def halves():

        for i in integers():
            yield i * 0.5

    def take(n, seq):
        res = []
        for _ in range(n):
            res.append(next(seq))
        return res

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))