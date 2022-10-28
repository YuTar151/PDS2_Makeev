# 2. Створіть функцію, яка приймає рядок з назвою файлу, створеного функцією з попереднього завдання.
# Функція має зчитувати файл, # записувати кожну пару ключ:значення у словник та повертати цей словник.

name = "Пори року.txt"
# def function(name):
with open(name, mode='r', encoding='utf8') as file:
    new_dict = {}
    for i in file:
        # new_dict.update(i)
        a, b = i.split(":")
        new_dict.update(f'{a}:{b}')

print(new_dict)
