#ДЗ 30. Перевірка на парність.
def is_even(number):
    binary_representation = bin(number)
    last_bit = binary_representation[-1]
    return last_bit == '0'

result = is_even(2494563894038**2)
print(result)
result = is_even(1056897**2)
print(result)
result = is_even(24945638940387**3)
print(result)
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('ok')