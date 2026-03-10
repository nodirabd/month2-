#родительский // сцпер класс ; наследники или  дочерний класс(подкласс)
class Car:
    def __init__(self, color, model):# initialization of features of the class object
        self.color = color
        self.model = model


    def drive_to(self, destination):
        print(f'Car {self.model} is going to {destination}  ')
    def change_color(self, new_color):
        self.color = new_color
class Bus(Car):
    def drive_to(self, destination):
        super().drive_to(destination)
        print(f'Bus  {self.model} is going to {destination} ')

bus_40 = Bus(color='red', model="Merce")
print(bus_40.color, bus_40.model)
bus_40.drive_to("Bishkek")


class Truck(Car):
    def drive_to(self, destination):

        print(f'Truck  {self.model} is going to {destination}  ')
truck_1 = Truck(color='navy blue', model = "Hyundai")
print(truck_1.color, truck_1.model)
truck_1.drive_to("Kara-Balta")