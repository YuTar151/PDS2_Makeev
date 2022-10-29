
# 5. Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається В ньому найчастіше?

# string = input("Задайте строку: ")
string = "Задайте строку: "
counted_chars = {}

for char in string:
    if char in counted_chars:
        counted_chars[char] += 1
    else:
        counted_chars[char] = 1

print(max(counted_chars))