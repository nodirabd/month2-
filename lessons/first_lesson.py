#code mini-exam 5th lesson
class Car:
    def __init__(self, color, model, year):# initialization of features of the class object
        self.color = color
        self.model = model
        self.year = year

    def drive_to(self, destination):
        print(f'Car {self.model} is going to {destination}  ')
#сlass для создания объекта, в нем описания объекта
car1 = Car(color = 'balck', model = 'Ford mustang', year = 2000)
car2 = Car(color = 'silver', model='Subary Forester', year = 2010)
print(f'Car 1 is {car1.color}, { car1.model},{car1.year}')
print(f'Car 2 is {car2.color}, {car2.model}')
car1.drive_to("Bishkek")
#self

car1.max_speed = 240
print(f'Car 1 has max speed of  {car1.max_speed} km/h')
