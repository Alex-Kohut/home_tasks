#ДЗ 15. Конвертер із числа в дату
#0 -> 0 днів, 00:00:00
#224930 -> 2 дні, 14:28:50
#466289 -> 5 днів, 09:31:29
#950400 -> 11 днів, 00:00:00
#1209600 -> 14 днів, 00:00:00
#1900800 - > 22 дні, 00:00:00
#8639999 -> 99 днів, 23:59:59
#22493 -> 0 днів, 06:14:53
#7948799 -> 91 день, 23:59:59
input_number = int(input('Enter num:'))
if input_number >= 0 and input_number <= 8640000:
    days = input_number // (24 * 3600)
    input_number %= (24 * 3600)
    hours = input_number // 3600
    input_number %= 3600
    minutes = input_number // 60
    input_number %= 60
    v_days = ()
    r_days = ()
    for i in range(1, 100, 10):
        if i != 11:
            v_days += (i,)
    for i in range(2, 94 + 1, 10):
        if i != 12 and 13 and 14:
            r_days += (i, i + 1, i + 2)

    result = ""
    if days >= 0:
        if days in v_days:
            result += f"{days} {'день '}"
        elif days in r_days:
            result += f"{days} {'дні '}"
        else:
            result += f"{days} {'днів '}"
        if hours > 0 or minutes > 0 or input_number > 0:
            result += ", "

    if hours > 0:
        result += f"{hours:02d}:{minutes:02d}:{input_number:02d}"
    else:
        result += f"{hours:02d}:{minutes:02d}:{input_number:02d}"

    print(result)
else:
    print('введіть число в діапазоні від 0 до 8640000')