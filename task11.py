#ДЗ 11. Модифікувати калькулятор
res = str(input('Do you want calculate something?'))
while res == 'yes':
    print(eval(input()))
    res = str(input('Do you want continue?'))