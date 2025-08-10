class vowels:
    def __init__(self, data: str):
        self.data: str = data
        self.idx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.idx < len(self.data):
            if self.data[self.idx].lower() in "aeoueiy":
                res = self.data[self.idx]
                self.idx += 1
                return res
            self.idx += 1
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)