from pathlib import Path
from string import punctuation

list_of_words_source = Path('words.txt')
input_file_source = Path('inputtext.txt')
output_file_source = Path('outputtext.txt')

result = {}

with open(list_of_words_source, 'r') as w:
    result = {word:0 for word in w.readline().split()}

with open(input_file_source, 'r') as i:
    for line in i.readlines():
        for word in line.split():
            word = word.strip(punctuation)
            if word.lower() in result:
                result[word.lower()] += 1

with open(output_file_source, 'w') as o:
    for word, count in sorted(result.items(), key=lambda x: -x[1]):
        o.write(f'{word} - {count}\n')

