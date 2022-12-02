"""
Напишите программу, которая ищет наибольший (не равный 1) общий делитель двух чисел, введённых пользователем (num_1, num_2),
и выводит его на экран. Если общих делителей нет, выводит на экран "Общих делителей не найдено".
Для проверки используйте num_1 = 1812, num_2 = 2500
PS: Если использовать break в цикле for - else, то при прерывании цикла код после else выполняться не будет.
"""

# num_1 = 1812
# num_2 = 2500
# a, b = 0, 0
# list = []
# i = 1
# for i in range(1, num_2):
# while num_1 < num_2:
#     a = num_1 % i
#     b = num_2 % i
#     if a == b and i !=1:
#         # print(i, end=" ")
#         list.append(i)
#         i += 1
# else:
#     print(list[-1])



"""
Напишите программу с использованием оператора continue, которая принимает на вход строку (string), после чего выводит её посимвольно,
но без букв а, б, в. Пример: ввод "арбуз", вывод "руз". Для проверки используйте string = 'абстракция'
PS: Чтобы выводить побуквенно в одну строчку, в фукнции print() предусмотрен параметр end. Если написать print('Hello!', end=''),
следующий print() продолжит вывод не с новой строки.
"""


#
# class DepartmentReport:
#     pass
#
#
# department_report = DepartmentReport


# class SalesReport():
#     def print_report(self):
#         print("Total amount", self.amount)
#
#
# report = SalesReport()
# report.amount = 10
#
# report_2 = SalesReport()
# report_2.amount = 20
#
#
# report.print_report()
# report_2.print_report()


# class ComplexNumber:
#     def __init__(self, r=0, i=0):
#         self.real = r
#         self.imag = i
#
#     def get_data(self):
#         print(f'{self.real}+{self.imag}j')


# Создаем новый объект ComplexNumber
# num1 = ComplexNumber(2, 3)

# Вызываем метод get_data()
# Вывод: 2+3j
# num1.get_data()

# Создаем еще один объект ComplexNumber
# и новый атрибут 'attr'
# num2 = ComplexNumber(5)
# num2.attr = 10

# Вывод: (5, 0, 10)
# print((num2.real, num2.imag, num2.attr))

# У объекта c1 нет атрибута 'attr', поэтому
# вызывается ошибка
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# print(num1.attr)

class TextProcessor:
    def init(self, text):
        self.text = text
        self.signs = signs = "?!. \'\"`,:;-_/()[]~"

    def __is_punktiantian(self):
        for letter in self.text:
            if letter in self.signs:
                return True
        for letter in self.text:
            if letter is not self.signs:
                return False


    def get_clean_string(self):
        if self.__is_punktiantian() == True:
            for test in self.signs:
                self.text = self.text.replace(test, '')
            return f" text corrected {self.text} "
        elif self.__is_punktiantian() == False:
            return f" text in normal {self.text} "
str_my = 'qwefsfdsr'
procc = TextProcessor(str_my)
ss = procc.get_clean_string()
print(ss)