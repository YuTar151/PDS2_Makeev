'''
1. Написати програму «Вгадай число». Комп'ютер генерує число від 1 до 100 і надає користувачеві б спроб, щоб він міг вгадати число.
Коли користувач вводить число у консолі, комп'ютер перевіряє, чи вiдповiдає воно заданому. Якщо число не вірне, то користувач отримує
повідомлення про те, менше чи бiльше число від заданого. Якщо користувач вгадав число, то йому повідомляється про перемогу і про
кiлькiсть використаних ним спроб. У разі вичерпання всіх спроб, користувач отримує повідомлення про програш. Перед написанням програми,
опишіть ïï алгоритм використовуючи псевдокод. Пiсля реалiзацiï коду, залиште псевдокод, як коментарі до нього.
'''

import random

def function(a):
    if a != number and a > number:
        print("Ні, не вгадав. Загадане число меньше від названного.")
        tryes -= 1

    elif a != number and a < number:
        print("Ні, не вгадав. Загадане число більше від названного.")
        tryes -= 1

    else:
        tryes2 = 6 - tryes
        print("Поздоровляю, ти вгадав. Використано спроб ", tryes2)

number = random.randint(0, 100)
tryes = 6
a = int(input("Добре, у тебе є 6 спроб. Вгадай яке число я загадав: "))

function(a)

Нужно доделать