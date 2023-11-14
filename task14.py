#ДЗ 14. Добуток чисел
#999 -> 2
#1000 -> 0
#423 -> 8
#33 -> 9
#25 -> 0
#1 -> 1

number = input("Введіть число: ")

digits = [int(digit) for digit in str(number)]

while len(digits) > 1:
    result = 1
    for digit in digits:
        result *= digit
    digits = [int(digit) for digit in str(result)]
print("Результат:", digits[0])