#ДЗ 23. Визначити популярність певних слів у тексті
def popular_words(text, words):

    text_lower = text.lower()
    words_in_text = text_lower.split()
    word_count = {word: 0 for word in words}
    total_words = len(words_in_text)

    for word in words_in_text:
        if word in word_count:
            word_count[word] += 1

    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')