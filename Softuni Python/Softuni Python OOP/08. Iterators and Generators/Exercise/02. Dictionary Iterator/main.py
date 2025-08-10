class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.data = dictionary
        self.keys = list(self.data.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        value = self.data[key]
        self.index += 1
        return (key, value)



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)