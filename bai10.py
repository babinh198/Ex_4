

from string import ascii_lowercase

words = ['python', 'patience', 'documents', 'students',
         'homework', 'practice', 'success', 'english',
         'university', 'congratulation']

result = []
for word in words:
    sum_value = 0
    for char in word:
        value = ascii_lowercase.index(char) + 1
        sum_value = sum_value + value
    result.append([word, sum_value])

print(result)
