"""
2, Напишіть програму, яка б приймала список з числами та перевіряла чи всі числа в ньому унікальні,
Реалізуйте у функції декілька обробок виключень,
"""
import sys
def test_list_exeptions(l):
        try:
            for i in l:
                i / 2
            n = len(l) - 1
            ts = set(l)
            ind = len(l) == len(ts)
            ind / ind
            print("Елементи списку унікальні")
        except TypeError:
            print("Один з елементів - не число!", file=sys.stderr)
        except ZeroDivisionError:
            print("В списку є однакові елементи", file=sys.stderr)


lst1 = [1, 2, 7, 6, 8, 3, 2, 5]
lst2 = [1, 2, 7, 6, "8", 3, 2, 5]
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list_exeptions(lst1)
test_list_exeptions(lst2)
test_list_exeptions(lst3)







