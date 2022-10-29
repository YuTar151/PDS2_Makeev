
# 3. Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово,
# яке однаково читається зліва направо та справа наліво. Наприклад, "випив".



def reverse_string2(word):
    res = ''.join(reversed(word.lower()))
    if word.lower() == res:
        w = True
    else:
        w = False
    return w

word = input('Введіть слово: ')
print(reverse_string2(word))