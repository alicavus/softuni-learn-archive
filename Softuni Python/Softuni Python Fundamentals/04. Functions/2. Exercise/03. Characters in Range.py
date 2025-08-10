def chars_in_range(char_one: str, char_two: str) -> str:
    return " ".join([chr(ch_code) for ch_code in range(ord(char_one) + 1, ord(char_two))])

print(chars_in_range(input(), input()))