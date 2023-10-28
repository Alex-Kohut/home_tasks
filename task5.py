#ДЗ 5. Розділити один список на два списки
my_list = [1, 2, 3, 4, 5, 6]
#my_list = [1, 2, 3, 4, 5]
#my_list = []

if len(my_list) == 0:
    list1 = list2 = my_list
elif len(my_list) % 2 == 0:
    list1 = my_list[0:(int(len(my_list)/2))]
    list2 = my_list[(int(len(my_list)/2)):(int(len(my_list)))]
else:
    list1 = my_list[0:(int(len(my_list)/2 + 1))]
    list2 = my_list[(int(len(my_list)/2 + 1)):(int(len(my_list)))]
new_list = [list1, list2]
print(new_list)
