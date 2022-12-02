"""
Додайте до попередньоï програми код, будь-якого алгоритму сортування. Додайте функцiю, яка б обраховувала середній
час роботи алгоритму сортування. Функцiя повинна приймати список i кiлькiсть iтерацiй циклiв сортування, а повертати
середній час роботи алгоритму сортування.
"""
import time
import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())


def selection_sort(data):
    global iter
    iter = 0
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
            iter += 1
    print("Selection Sort:", data)
    print("Iterations: ", iter)


laps = 0
Duration_time = 0

while laps < 10:
    copy_my_list = int_list
    cur_time = time.time()
    selection_sort(copy_my_list)
    print(f"Duration time (int_list): {time.time() - cur_time}")
    laps += 1
    Duration_time += time.time() - cur_time
else:
    sorting_int_list = Duration_time / 10
    int_list_iter = copy.iter



laps = 0
Duration_time = 0

while laps < 10:
    copy_my_list = float_list
    cur_time = time.time()
    selection_sort(copy_my_list)
    print(f"Duration time (float_list): {time.time() - cur_time}")
    laps += 1
    Duration_time += time.time() - cur_time
else:
    sorting_float_list = Duration_time / 10
    float_list_iter = iter


laps = 0
Duration_time = 0

while laps < 10:
    copy_my_list = str_list
    cur_time = time.time()
    selection_sort(copy_my_list)
    print(f"Duration time (str_list): {time.time() - cur_time}")
    laps += 1
    Duration_time += time.time() - cur_time
else:
    sorting_str_list = Duration_time / 10
    str_list_iter = iter
    print("Summary:")
    print(f"Average time sorting int_list: {sorting_int_list}, iterations = {int_list_iter}")
    print(f"Average time sorting float_list: {sorting_float_list}, iterations = {float_list_iter}")
    print(f"Average time sorting str_list: {sorting_str_list}, iterations = {str_list_iter}")


