class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    @property
    def idx(self):
        return self.__idx
    
    @idx.setter
    def idx(self, value):
        if value >= len(self.sequence):
            value %= len(self.sequence)
        self.__idx = value

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= 0:
            raise StopIteration()
        res = self.sequence[self.idx]
        self.number -= 1
        self.idx += 1
        return res


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
print()
for item in result:
    print(item, end ='')
