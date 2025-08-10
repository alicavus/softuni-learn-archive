from math import trunc
class Integer:
    def __init__(self, value: int):
        self.value: int = value
    
    @classmethod
    def from_float(cls, float_value: float):
        if isinstance(float_value, float):
            return cls(value = trunc(float_value))
        return "value is not a float"
    
    @classmethod
    def from_roman(cls, value: str):
        ROMAN_NUMERALS = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        total: int = 0
        prev: int = 0

        for numeral in value[::-1]:
            try:
                cur = ROMAN_NUMERALS[numeral]
            except IndexError:
                return "wrong numeral"
            else:
                total += cur if cur >= prev else -cur
                prev = cur
        return cls(total)
    
    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except:
                return "wrong type"
        return "wrong type"

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))