
# 3. Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово,
# яке однаково читається зліва направо та справа наліво. Наприклад, "випив".


word = input('Введіть слово: ')

def reverse_string2(s):
    return "".join(reversed(s))

word2 = reverse_string2(word.lower())
if word.lower() == word2:
    print(True)
else:
    print(False)