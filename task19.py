#ДЗ 19. Пошук спільних елементів
def common_elements():

    multiples_of_3 = [num for num in range(1, 51) if num % 3 == 0]

    multiples_of_5 = [num for num in range(1, 101) if num % 5 == 0]

    set_of_multiples_of_3 = set(multiples_of_3)
    set_of_multiples_of_5 = set(multiples_of_5)

    common_set = set_of_multiples_of_3.intersection(set_of_multiples_of_5)

    return common_set

result = common_elements()

print("Перетин множин:", result)