# 5. Напишіть код, який просить ввести дві будь-яких змінних, а потім міняє їх МІСЦЯМИ.
a = input("Введіть число 1: ")
b = input("Введіть число 2: ")
a, b = b, a
print('Число 1', a)
print('Число 2', b)