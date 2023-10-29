#ДЗ 7. Перемістити всі нулі до кінця списку
# lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = []
# lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

el = 0
for el in lst:
    if  el == 0:
        i = lst.index(el)
        lst.pop(i)
        lst.append(0)
print(lst)

