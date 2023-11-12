#ДЗ 10. Ім'я змінної
import string
import keyword
new_string = str(input('Enter name of variable:'))
valid_characters = string.ascii_lowercase + string.digits + "_"

if new_string[0].isdigit():
    print('False')
elif new_string.isdigit():
    print('False')
elif any(char not in valid_characters for char in new_string):
    print('False')
elif keyword.iskeyword(new_string):
    print('False')
else:
    print('true')




