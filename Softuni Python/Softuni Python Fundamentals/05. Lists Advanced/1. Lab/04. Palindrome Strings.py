my_words = input().split()
word = input()

palindromes = [x for x in my_words if x == x[::-1]]

print(palindromes, f'Found palindrome {palindromes.count(word)} times', sep='\n')