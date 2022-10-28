# 2. Створіть список, що містить числа від 0 до 100 та за допомогою List Comprehension отримайте з нього список чисел, що кратні 3.
my_list = [i for i in range(101) if i % 3 == 0]
print(my_list)