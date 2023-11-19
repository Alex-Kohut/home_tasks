#ДЗ 21. Паліандром
import string
def is_palindrome(text):

        text = text.replace(" ", "").lower()
        text = ''.join(char for char in text if char not in string.punctuation)
        return text == text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
