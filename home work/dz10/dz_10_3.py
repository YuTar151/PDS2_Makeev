"""
3. Напишіть користувацький клас виключення з функціоналом на свій вибір. Викличте його за допомогою інструкції raise.
"""
import sys

class MyCustomErrors:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def division(self):
        try:
           res = self.a / self.b / self.c
           print(res)
        except SyntaxError as ex:
            print("Якась синтаксична помилка", file=sys.stderr)
            print(ex)
        except ZeroDivisionError as ex:
            print("В одній із змінних є 0. На який ділити не можна", file=sys.stderr)
            print(ex)
        except TypeError as ex:
            if self.a is not isinstance(self.a, int) or self.b is not isinstance(self.b, int) or self.c is not isinstance(self.c, int):
                print("Одна із змінних не є числом. Введіть три числа будь ласка", file=sys.stderr)
                print(ex)
            else:
                print("Виникла непередбачена помилка", file=sys.stderr)
                print(ex)


begin = MyCustomErrors(3, 2, 5)
print(begin.division())
raise TypeError


