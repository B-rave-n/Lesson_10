def first_word(text):
    # Ця функція проходить тести, але складна і специфічна під кокретне завдання
    # нижче буде функція, яка більш універсальна
    words = text.split()
    firstword = None
    for i in words:
        for j in i:
            if j.isalpha():
                firstword = i.split('.')[0]
                break
        if firstword:
            break

    lst = list(firstword)
    for i in lst:
        if not i.isalpha():
            lst.remove(i)
        else:
            break
    for i in lst[::-1]:
        if not i.isalpha():
            lst.pop()
        else:
            break
    firstword = ''.join(lst)
    return firstword

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('Усі тести успішно пройдені!')

import re

def first_word(text):
    # Шукаємо в тексті рядок, який складається із літер або символу '
    match = re.search(r"[a-zA-Z']+", text)
    # Якщо знайшли, то повертаємо його рядком
    if match:
        return match.group(0)
    # На випадок, якщо не було нічого знайдено
    return ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('Усі тести успішно пройдені!')
