"""
3. Напишіть клас Parallelogram, який приймає два аргументи width i length i метод get_area, який вираховує площу
паралелограму. Успадкуйте від нього клас Square, перевизначіть в ньому метод get_area таким чином, щоб він
вираховував площу квадрату.
"""

class Parallelogram:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Square(Parallelogram):

    def get_area(self):
        return (self.width * self.length)**2


area = Parallelogram(5, 8)
print(area.get_area())

area = Square(5, 8)
print(area.get_area())
