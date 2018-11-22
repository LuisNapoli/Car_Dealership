import os
from car import Car

class Dealership:
    def __init__(self,name):
        self.name = name
        self.cars = []
        if os.path.exists(f'{self.name}.txt'):
            file = open(f'{self.name}.txt','r')
            for cr in file.readlines():
            #duvida aqui
        else:
            file = open(f'{self.name}.txt','w')
        file.close()


    def get_name(self):
        return self.name

    def get_cars(self):
        return self.cars

    def add_car(self,car):
        self.cars.append(car)

    def save_cars(self):
        file = open(f'{self.name}.txt', 'w')
        for cr in self.cars:
            file.write(str(c.get_data()))
            file.write('\n')
        file.close()
