from string import ascii_uppercase, ascii_lowercase

class Game:
    def __init__(self, strings: str):
        self.strings = strings.split()
        self.points = 0

        for string in self.strings:
            self.points += self.calculate(string)
    
    def __repr__(self):
        return f'{self.points:.2f}'
    
    def calculate(self, string: str):
        first_char, last_char, number = string[0], string[-1], int(string[1:-1])

        if first_char in ascii_lowercase:
            number *= ascii_lowercase.index(first_char) + 1

        elif first_char in ascii_uppercase:
            number /= ascii_uppercase.index(first_char) + 1
        
        if last_char in ascii_lowercase:
            number += ascii_lowercase.index(last_char) + 1

        elif last_char in ascii_uppercase:
            number -= ascii_uppercase.index(last_char) + 1
        
        return number

if __name__ == "__main__":
    game = Game(strings=input())
    print(game)