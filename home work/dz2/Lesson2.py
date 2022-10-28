# ######
# DIGITS
# ######

a = 10
b = 1.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(-a)

# #######
# STRINGS
# #######

string = "Hello, World!"
print(string[0])
print(string.upper())
print(string.lower())
print(string + "!!")
print(string.replace(" ", ""))

# ###########
# COLLECTIONS
# ###########

my_list = [1, "two", 3.0]
print(my_list[1])
my_list.remove("two")
print(my_list)

my_dict = {1: "one1", 2: "two2"}
print(my_dict[1])

# #########
# FIFO LIFO
# #########

queue = list()
queue.append(1)
queue.append(2)
queue.append(3)

'''
print(queue.pop(0))  # 1
print(queue.pop(0))  # 2
print(queue.pop(0))  # 3
'''

print(queue.pop())  # 3
print(queue.pop())  # 2
print(queue.pop())  # 1
