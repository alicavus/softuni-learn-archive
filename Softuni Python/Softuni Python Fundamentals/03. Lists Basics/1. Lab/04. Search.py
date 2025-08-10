number_of_words = int(input())

word_to_find = input()

words = [input() for _ in range(number_of_words)]
words_that_contain_search_word = []

print(words, [x for x in words if word_to_find in x], sep="\n")

