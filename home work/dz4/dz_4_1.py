
# 1. Напишіть функцію, яка приймає Номер місяця та повертає рядок з назвою пори року, до якої цей місяць відноситься.

m_number = int(input('Вкажіть номер: '))

def seasons(m_number):
    mounth_dic = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Літо', 7:'Літо', 8:'Літо', 9:'Осінь', 10:'Осінь', 11:'Осінь', 12:'Зима'}
    return mounth_dic.get(m_number)

seasons(m_number)

print(seasons(m_number))
