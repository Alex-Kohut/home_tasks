#ДЗ 6. Перемістити елемент у списку
my_list = [1, 2, 3, 4, 5, 6]
#my_list = [1]
#my_list = []

if len(my_list) == 0:
    print(my_list)
elif len(my_list) > 1:
    last_num = (my_list[-1])
    my_list.insert(0, last_num)
    my_list.pop()
    print(my_list)
else:
    print (my_list)
