class RageQuit:
    def __init__(self, string: str):
        self.string = ""
        cur_string = ""
        cur_number = ""
        prev_char = ""
        for char in string:
            if not char.isdigit():
                if prev_char.isdigit():
                    self.string += cur_string.upper() * int(cur_number)
                    cur_number = ""
                    cur_string = ""
                cur_string += char
            elif char.isdigit():
                cur_number += char
            prev_char = char
        self.string += cur_string.upper() * int(cur_number)
    
    def __str__(self):
        return f"Unique symbols used: {len(set([char for char in self.string]))}\n{self.string}"


if __name__ == "__main__":
        rage = RageQuit(string=input())
        print(rage)