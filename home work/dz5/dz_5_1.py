# 1. Напишіть функцію, яка отримує Словник та назву у рядку, а потім створює файл з цією назвою, який містить всі
# дані з цього словника. Один рядок — одна пара ключ:Значення.

def my_func(di, name):
    with open(name, mode='w', encoding="utf-8") as file:
        for k, v in di.items():
            string = f'{k}:{v}\n'
            file.write(str(string))

    file.close()

di = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Літо', 7:'Літо', 8:'Літо', 9:'Осінь', 10:'Осінь', 11:'Осінь', 12:'Зима'}
name = "Пори року.txt"

my_func(di, name)





