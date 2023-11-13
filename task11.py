#ДЗ 11. Модифікувати калькулятор
res = str(input('Do you want calculate something?'))

while res == 'yes':
    number1 = int(input('Enter first num:'))
    number2 = int(input('Enter second num:'))
    math_operation = input('Enter math operation')
    if math_operation == '+':
        print(number1 + number2)
    elif math_operation == '-':
        print(number1 - number2)
    elif math_operation == '*':
        print(number1 * number2)
    elif math_operation == '/' and number2 != 0:
        print(number1 / number2)
    else:
        print('wrong operation!!!')
    res = str(input('Do you want calculate something?'))
else:
    print('finish')