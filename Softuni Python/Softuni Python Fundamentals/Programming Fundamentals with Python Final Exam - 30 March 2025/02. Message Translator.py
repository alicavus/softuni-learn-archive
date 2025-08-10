import re

class Translator:
    __pattern = r'\!([A-Z][a-z]{2,})\!\:\[([A-Za-z]{8,})\]'

    def __init__(self, string: str):
        self.string = string

        pattern_matches = re.findall(Translator.__pattern, self.string)

        if pattern_matches == []:
            print("The message is invalid")
            return
        
        #print(pattern_matches)
        print(f'{pattern_matches[0][0]}: {self.translator(pattern_matches[0][1])}')
    
    def translator(self, string: str):
        return " ".join([f'{ord(char)}' for char in string])

for _ in range(int(input())):
    Translator(input())