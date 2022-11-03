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
# # for i in range(1, num_2):
# while num_1 < num_2:
#     a = num_1 % i
#     b = num_2 % i
#     if a == b and i !=1:
#         print(i, end=" ")
#         list.append(i)
#     i += 1
#     # else:
# print(list[-1])


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


class SalesReport():
    def __init__(self):
        self.deals = None

    def add_deal(self, amount):
        if not hasattr(self, "deals"):
            self.deals = []
        self.deals.append(amount)

    def total_amount(self):
        return sum(self.deals)

    def print_report(self):
        print("Total sales", self.total_amount())