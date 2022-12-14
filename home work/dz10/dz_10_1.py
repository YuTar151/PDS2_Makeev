"""
1. Напишіть функцію, яка б приймала номер місяця, а вертала його назву. Реалізуйте у функцiï декілька обробок виключень.
"""
import sys
def mounth(num):
    mounth_dict = {1:"січень", 2:"лютий", 3:"березень", 4:"квітень", 5:"травень", 6:"червень", 7:"липень", 8:"серпень", 9:"Вересень", 10:"жовтень", 11:"листопад", 12:"грудень"}
    try:
        num = int(num)
        if num <= 0 or num > 12:
            print("Треба вказати число від 1 до 12", file=sys.stderr)
        else:
            print(mounth_dict.get(num))
    except ValueError as ex:
        print("Треба ввести ціле цисло", file=sys.stderr)
        print(ex)
    except SyntaxError as ex:
        print("Синтаксична помилка, виправте та спробуйте ще.", file=sys.stderr)
        print(ex)


num = input("Введіть номер місяця: ")
mounth(num)