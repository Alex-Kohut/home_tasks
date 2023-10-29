# ДЗ 8. Знайти суму елементів із парними індексами
first_list = [0, 1, 7, 2, 4, 8]
#first_list = [1, 3, 5]
#first_list = [6]
#first_list = []

second_list = []
if len(first_list) == 0:
    print(0)
else:
    for el in first_list:
        if first_list.index(el) % 2 == 0:
            second_list.append(el)
    sun_nums_multiplied = sum(second_list) * first_list[-1]
    print(sun_nums_multiplied)
