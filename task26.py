import re
def first_word(s):

    s = re.sub(r'^[^a-zA-Z\']*', '', s)

    match = re.match(r"[a-zA-Z']+|[^a-zA-Z']+.*", s)

    if match:
        return match.group(0)
    else:
        return None

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')