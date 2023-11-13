#ДЗ 13. Діапазон букв
#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA
import string
user_input = input("Введіть дві літери через дефіс: ")
a = user_input[0]
b = user_input[-1]
start_index = string.ascii_letters.index(a)
end_index = string.ascii_letters.index(b)

if start_index > end_index:
    start_index, end_index = end_index, start_index

result = string.ascii_letters[start_index:end_index + 1]
print(result)