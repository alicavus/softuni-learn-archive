class take_skip:
    def __init__(self, step: int, count: int):
        self.step: int = step
        self.count: int = count
        self.curr: int = 0
    

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr == self.count:
            raise StopIteration()
        res = self.curr * self.step
        self.curr += 1
        return res


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print("---")
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
