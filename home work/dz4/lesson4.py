
import copy


'''
def my_function(arg):
    return arg


print(my_function(2))
'''

'''
x = lambda a: a * 3
print(x(10))  # 30

print("String is an argument for print function")

int_variable = int("1")  # Returns int value
'''

'''
def my_function(a):
    a += 1


print(my_function(2))
'''


'''
def my_function(a):
    pass


print(my_function(2))
'''


'''
def my_function(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)


print(my_function(b=8))
'''


'''
def my_function(*args):
    for i in args:
        print(i)


print(my_function(1, 2, 3))
'''


'''
def my_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


my_function(a=1, b=2, c=3)
'''


'''
def my_function(a, b, *, flag=True):
    print(flag)


my_function(1, 2, flag=True)
'''


'''
a = 1


def my_function(a):
    a+=1
    print(a)

my_function(copy.copy(a))
print(a)
'''


'''
def descending(i):
    while i > 0:
        yield i
        i -= 1

for i in descending(10):
    print(i)
'''


'''
l = list(range(10))
print(type(l))
print(l[0])
'''

'''
def recursion():
    password = input("Type pass: ")
    if password != "12345":
        recursion()


recursion()
'''
Lesson4.py
Lesson4.py. На экране.