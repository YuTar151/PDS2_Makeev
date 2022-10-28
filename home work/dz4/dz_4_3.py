
# 3. Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово,
# яке однаково читається зліва направо та справа наліво. Наприклад, "випив".



def reverse_string2(word):
    word = reversed(word)
    word2 = word.lower()
    if word.lower() == word2:
        print(True)
    else:
        print(False)
    return

word = input('Введіть слово: ')
print(reverse_string2(word))