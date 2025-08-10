class Exploder:
    __exploder = '>'
    def __init__(self, string: str):
        self.__string = string
        self.__strength = 0

        exploded_string = ""

        prev_char = None
        for char in self.__string:
            if prev_char == Exploder.__exploder:
                self.__strength += int(char)
            
            if self.__strength and char != Exploder.__exploder:
                    self.__strength -= 1

            else:
                exploded_string += char
            
            prev_char = char
        
        self.__string = exploded_string
    
    def __str__(self):
        return self.__string

if __name__ == "__main__":
    exploder = Exploder(string=input())
    print(exploder)