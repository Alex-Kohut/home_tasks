#ДЗ 18. Пошук підрядка
def second_index(string, target):
    first_occurrence = string.find(target)

    if first_occurrence != -1:
        second_occurrence = string.find(target, first_occurrence + 1)

        if second_occurrence != -1:
            return second_occurrence

    return None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
