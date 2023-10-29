#ДЗ 9. Список із 3 елементів
import random
random_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]
print(random_list)
new_list = [random_list[0], random_list[2], random_list[-2]]
print(new_list)