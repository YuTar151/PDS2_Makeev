
# 5. Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається В ньому найчастіше?

def letter_stat(string):
    counted_chars = {}
    for char in string:
        if char in counted_chars:
            counted_chars[char] += 1

        else:
            counted_chars[char] = 1

    a = max(counted_chars.values())
    for k, v in counted_chars.items():
        if v >= a:
            res = f"Літера '{k}', зустрічається найчастіше ({v} рази)"
            return res

string = input("Задайте строку: ")
string = string.replace(" ", "")
string = string.replace(",", "")
string = string.replace(".", "")
string = string.replace("!", "")

print(letter_stat(string))