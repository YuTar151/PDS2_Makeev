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


class SalesReport():
    # Будем принимать в __init__ ещё и имя менеджера
    def __init__(self, manager_name):
        self.deals = []
        self.manager_name = manager_name

    def add_deal(self, amount):
        self.deals.append(amount)

    def total_amount(self):
        return sum(self.deals)

    def print_report(self):
        # И добавлять это имя в отчёт
        print("Manager:", self.manager_name)
        print("Total sales:", self.total_amount())


report = SalesReport("Ivan Taranov")
report.add_deal(10_000)
report.add_deal(30_000)
report.print_report()
# =>
# Manager: Ivan Taranov
# Total sales: 40000