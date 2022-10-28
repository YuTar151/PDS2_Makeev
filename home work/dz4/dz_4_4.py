# 4. Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.
# number = input("Введіть число: ")

number = input("Введіть число: ")
nlist = list(number)
def function(nlist):
    summ = 0
    for i in nlist:
        summ += int(i)
    return summ

function(nlist)

print(function(nlist))