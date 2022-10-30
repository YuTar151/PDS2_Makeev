# 3. Напишіть функцію, яка роздруковує всі файли та каталоги поточного каталогу, а також їх кількість окремо. Назви каталогів повинні мати позначення “І"

import os

def filesys():
    path = os.getcwd()
    cat_counter = 0
    file_counter = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for dirname in dirnames:
            print(f'Каталог: |{dirname}')
            cat_counter += 1

        for filename in filenames:
            print("Файл:", filename)
            file_counter += 1

    print(f'Каталогів всього: {cat_counter} шт.')
    print(f'Файлів всього: {file_counter} шт.')


filesys()