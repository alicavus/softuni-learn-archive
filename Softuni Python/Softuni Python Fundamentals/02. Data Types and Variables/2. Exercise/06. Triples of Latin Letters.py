from string import ascii_lowercase as latin_alphabet

n = int(input())

for ix1 in range(n):
    for ix2 in range(n):
        for ix3 in range(n):
            print(f"{latin_alphabet[ix1]}{latin_alphabet[ix2]}{latin_alphabet[ix3]}")