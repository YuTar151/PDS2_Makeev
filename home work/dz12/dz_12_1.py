"""
1. Створіть функцiю, яка обчислює факторіал числа. Запустіть декілька задач, що використовуватимуть ThreadpoolExecutor.
Виміряти швидкість обчислень. Зробіть теж саме, використовуючи ProcessPoolExecutor. Додайте у програму код,
який порівнює швидкість обчислень і виводить на Друк найоптимальніший метод.
"""
import threading
from multiprocessing import Process
import time

def factorial(n):
    global result
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


start_time1 = time.time()
task1 = threading.Thread(target=factorial, args=(50,)).start()
end_time1 = time.time() - start_time1
# print(f"Факторіал заданного числа = {result}")
print(f"На обчислення результату за допомогою threading пішло {end_time1} часу")


if __name__ == '__main__':
    start_time2 = time.time()
    proc1 = Process(target=factorial, args=(50,)).start()
    end_time2 = time.time() - start_time2
    # print(f"Факторіал заданного числа = {result}")
    print(f"На обчислення результату за допомогою multiprocessing пішло {end_time2} часу")

    if end_time1 > end_time2:
        res = end_time1 - end_time2
        print(f"Метод multiprocessing швидше на {res} сек")
    else:
        res = end_time2 - end_time1
        print(f"Метод threading швидше на {res} сек")





