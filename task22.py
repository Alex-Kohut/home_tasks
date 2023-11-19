#ДЗ 22. Унікальне число
def find_unique_value(numbers):
    count_dict = {}

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    unique_value = None
    for key, value in count_dict.items():
        if value == 1:
            unique_value = key
            break

    return unique_value
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
