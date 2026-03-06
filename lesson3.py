class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__fined = False
        self.__max_speed = 100

    def _test(self):
        print(f"Test car color:{self.color}, {self.__fined}")

    def __test2(self):
        print(f"Test private method {self.__max_speed}")

    def drive_to(self, destination):
        if not self.__fined:
            print(f"Машина {self.model} едет в {destination}, max speed {self.__max_speed}")
        else:
            print("Машина оштрафована")
        self.__test2()

    def change_color(self, new_color):
        self.color = new_color


car_mustang = Car(color='black', model='Ford Mustang')
car_mustang._test()
print(car_mustang.color)
car_mustang.drive_to('Karakol')
print(car_mustang._Car__max_speed) # нельзя оставлять такой код, это просто для проверок
# print(car_mustang.__max_speed) # ошибка - доступ к приватному атрибуту
# car_mustang.__test2()
car_mustang.__max_speed = 50 # так делать неправильно, может привести к ошибкам
car_mustang.drive_to('Karakol')