class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "GAV-GAV!!!"


class Cat(Animal):
    def make_sound(self):
        return "MIU MIU"



dog = Dog("Sharik", 3)
cat = Cat("Murka", 1)
print(f"{dog.get_name()}  give a sound: {dog.make_sound()}")
print(f"{cat.get_name()} give a sound: {cat.make_sound()}")
print()
print(f"Previous name of cat is : {cat.get_name()}")
cat.set_name("Kisa")
print(f"New name of cat is: {cat.get_name()}")
print(f"Previous age of cat is : {cat.get_age()}")
cat.set_age(2)
print(f"New age of cat is: {cat.get_age()}")
print()
print(f"Previous name of dog is : {dog.get_name()}")
dog.set_name("Rex")
print(f"New name of dog is: {dog.get_name()}")
print(f"Previous age of dog is : {dog.get_age()}")
dog.set_age(2)
print(f"New age of dog is: {dog.get_age()}")
