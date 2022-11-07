"""
1. Напишіть клас автомобіля з атрибутами:
• марка, колір, об'єм двигуна.
Та методами:
• їхати вперед, їхати назад.

Напишіть ще один клас автомобіля, який є успадкованим від першого.
Додайте в нього методи повороту праворуч та ліворуч.
"""

class Car:

    def __init__(self, car_model="", color="", engine_volume=0):
        self.car_model = car_model
        self.color = color
        self.engine_volume = engine_volume


    def go_ahead(self):
        print(f"{self.color} {self.car_model} V{self.engine_volume} їде вперед")
        # print("їде вперед")


    def go_back(self):
        print(f"{self.color} {self.car_model} V{self.engine_volume} їде назад")
        # print("їде назад")

class Car2(Car):


    def turn_left(self):
        print(f"{self.color} {self.car_model} V{self.engine_volume} повертає на ліво")
        # print("повертає на ліво")


    def turn_right(self):
        print(f"{self.color} {self.car_model} V{self.engine_volume} повертає на право")
        # print("повертає на право")


drive = Car2("Tesla", "Синя", 2.8)
drive.turn_right()
drive.turn_left()
drive.go_ahead()
drive.go_back()
