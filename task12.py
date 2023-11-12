#ДЗ 12. hashtag
import string
input_string = input("Введіть рядок: ")
input_string = ''.join(char for char in input_string if char not in string.punctuation)
hashtag = '#' + ''.join(word.capitalize() for word in input_string.split())
hashtag1 = hashtag[:140]
print("Hashtag:", hashtag1)



