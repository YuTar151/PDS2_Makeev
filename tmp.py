def count_words(data):
    word_counter = len(data.split(' '))
    return word_counter


data = "2. Додайте до серверу з першого завдання функцiю чат-боту який би відсилав клієнту задані відповіді на певні повідомлення"
print(count_words(data))