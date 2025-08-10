class Manipulator:
    def __init__(self, string: str):
        self.string = string
    
    def __str__(self):
        return self.string
    
    def translate(self, char: str, replacement: str):
        self.string = self.string.replace(char, replacement)
        return self.string

    def includes(self, substring: str):
        return substring in self.string
    

    def start(self,  substring: str):
        return self.string.startswith(substring)

    def lowercase(self):
        self.string = self.string.lower()
        return self.string

    def findindex(self, char: str):
        idx = -1
        for index, character in enumerate(self.string):
            if character == char:
                idx = index
        
        return idx

    def remove(self, start_index: int, count: int):
        self.string = self.string[:start_index] + self.string[start_index+count:]
        return self.string

m = Manipulator(input())
while True:
    commands = input().split()

    match commands[0]:
        case "End":
            break
        case "Translate":
            res = m.translate(commands[1], commands[2])
        case "Includes":
            res = m.includes(commands[1])
        case "Start":
            res = m.start(commands[1])
        case "Lowercase":
            res = m.lowercase()
        case "FindIndex":
            res = m.findindex(commands[1])
        case "Remove":
            res = m.remove(int(commands[1]), int(commands[2]))
    
    print(res)