# 4. Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.
# number = input("Введіть число: ")



def function(nlist):
    summ = 0
    for i in nlist:
        summ += int(i)
    return summ

number = input("Введіть число: ")
nlist = list(number)

print(function(nlist))