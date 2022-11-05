# class DepartmentReport():
#     def __init__(self):
#         self.deals = []
#
#     def add_revenue(self, amount):
#         if not hasattr(self, "deals"):
#             self.deals = []
#         self.deals.append(amount)
#
#     def total_amount(self):
#         return sum(self.deals)
#
#     def average_revenue(self):
#         return sum(self.deals) / len(self.deals)
#         # print("Average revenue", self.total_amount())
#
#     def revenues(self):
#         return self.deals
#         # print(self.deals)
#
#
# report = DepartmentReport()
# report.add_revenue(1_000_000)
# report.add_revenue(400_000)
# print(report.revenues())  # => [1000000, 400000]
# print(report.average_revenue()) # => 700000.0


# class SalesReport():
#     # Будем принимать в __init__ ещё и имя менеджера
#     def __init__(self, manager_name):
#         self.deals = []
#         self.manager_name = manager_name
#
#     def add_deal(self, amount):
#         self.deals.append(amount)
#
#     def total_amount(self):
#         return sum(self.deals)
#
#     def print_report(self):
#         # И добавлять это имя в отчёт
#         print("Manager:", self.manager_name)
#         print("Total sales:", self.total_amount())
#
#
# report = SalesReport("Ivan Taranov")
# report.add_deal(10_000)
# report.add_deal(30_000)
# report.print_report()
# # =>
# # Manager: Ivan Taranov
# # Total sales: 40000


# class DepartmentReport():
#     def __init__(self, company_name):
#         self.deals = []
#         self.company_name = company_name
#
#     def add_revenue(self, amount):
#         if not hasattr(self, "deals"):
#             self.deals = []
#         self.deals.append(amount)
#
#     def total_amount(self):
#         return sum(self.deals)
#
#     def revenues(self):
#         return self.deals
#
#     def average_revenue(self):
#         res = sum(self.deals) / len(self.deals)
#         # print(f"Average department revenue for {self.company_name}: {round(res)}")
#         return f"Average department revenue for {self.company_name}: {round(res)}"
#
#
# report = DepartmentReport("Danon")
# report.add_revenue(1_000_000)
# report.add_revenue(400_000)
# print(report.average_revenue())     # => Average department revenue for Danon: 700000


# class SalesReport():
#     def __init__(self, employee_name):
#         self.deals = []
#         self.employee_name = employee_name
#
#     def add_deal(self, company, amount):
#         self.deals.append({'company': company, 'amount': amount})
#
#     def total_amount(self):
#         return sum([deal['amount'] for deal in self.deals])
#
#     def average_deal(self):
#         return self.total_amount() / len(self.deals)
#
#     def all_companies(self):
#         return list(set([deal['company'] for deal in self.deals]))
#
#     def print_report(self):
#         print("Employee: ", self.employee_name)
#         print("Total sales:", self.total_amount())
#         print("Average sales:", self.average_deal())
#         print("Companies:", self.all_companies())
#
#
# report = SalesReport("Ivan Semenov")
#
# report.add_deal("PepsiCo", 120_000)
# report.add_deal("SkyEng", 250_000)
# report.add_deal("PepsiCo", 20_000)
#
# report.print_report()
# # => Employee:  Ivan Semenov
# # Total sales: 390000
# # Average sales: 130000.0
# # Companies: ['PepsiCo', 'SkyEng']


class Client():
    # Базовые данные
    def __init__(self, email, order_num, registration_year):
        self.email = email
        self.order_num = order_num
        self.registration_year = registration_year
        self.discount = 0

        # Оформление заказа

    def make_order(self, price):
        self.update_discount()
        self.order_num += 1
        # Здесь было бы оформления заказа, но мы просто выведем его цену
        discounted_price = price * (1 - self.discount)
        print(f"Order price for {self.email} is {discounted_price}")

        # Назначение скидки

    def update_discount(self):
        if self.registration_year < 2018 and self.order_num >= 5:
            self.discount = 0.1

        # Применение


# Сделаем подобие базы
client_db = [
    Client("max@gmail.com", 2, 2019),
    Client("lova@yandex.ru", 10, 2015),
    Client("german@sberbank.ru", 4, 2017)
]

# Сгенерируем заказы
client_db[0].make_order(100)
# => Order price for max@gmail.com is 100

client_db[1].make_order(200)
# => Order price for lova@yandex.ru is 180.0

client_db[2].make_order(500)
# => Order price for german@sberbank.ru is 500

client_db[2].make_order(500)
# => Order price for german@sberbank.ru is 450.0

"""
Определите класс для пользователей User:
у него должны быть атрибуты email, password и balance, которые устанавливаются при инициализии;
у него должен быть метод login, который принимает емейл и пароль, если они совпадают с атрибутами объекта,он возвращает True, а иначе Fals;
должен быть метод update_balance(amount), который изменяет баланс счёта на величину amount.
В случае правильного описания класса код, приведённый ниже, должен выдать следующий результат:
"""

user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")    # => False
user.login("gosha@roskino.org", "qwerty")   # => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)     # => 19700
