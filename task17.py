#ДЗ 17. Модифікувати рядок
def correct_sentence(sentence):

    if len(sentence) == 0:
        return ""

    corrected_sentence = sentence[0].capitalize() + sentence[1:]
    if corrected_sentence[-1] != '.':
       corrected_sentence += '.'
    return corrected_sentence

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
