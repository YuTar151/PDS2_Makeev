# 2. Створіть функцію, яка приймає рядок з назвою файлу, створеного функцією з попереднього завдання.
# Функція має зчитувати файл, # записувати кожну пару ключ:значення у словник та повертати цей словник.

def function(name):
    with open(name, mode='r', encoding='utf8') as file:
        new_dict = {}
        for i in file:
            a, b = i.split(":")
            new_dict[a] = b.replace("\n", "")
    print(new_dict)
    return

name = "Пори року.txt"
function(name)