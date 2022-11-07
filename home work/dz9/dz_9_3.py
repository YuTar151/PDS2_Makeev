"""
3. Напишіть клас Parallelogram, який приймає два аргументи width i length i метод get_area, який вираховує площу
паралелограму. Успадкуйте від нього клас Square, перевизначіть в ньому метод get_area таким чином, щоб він
вираховував площу квадрату.

base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)
"""

class Parallelogram:

    def __init__(self, width, length):
        self.width = width
        self.length = length


    def get_area(self):
        res = self.width * self.length
        print(res)

area = Parallelogram(8, 5)
area.get_area()
