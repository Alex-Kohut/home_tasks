# ДЗ 4. Найпростіший калькулятор
number1 = int(input('Enter first num:'))
number2 = int(input('Enter second num:'))
math_operation = input('Enter math operation')
if math_operation == '+':
    print(number1+number2)
elif math_operation == '-':
    print(number1-number2)
elif math_operation == '*':
    print(number1 * number2)
elif math_operation == '/' and number2 != 0:
    print(number1 / number2)
else:
    print('wrong operation!!!')
