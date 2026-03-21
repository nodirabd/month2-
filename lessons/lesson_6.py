#git branch показывает на какой ветке
"""слияние merge
pull request
git pull origin main  """
""" magic когда мы их вызываем они сами срабатывают
from lessons.money import Money
money_1 = Money(10, 'USD'
print(money_1)"""
class Animal:
    def move(self):
        print('animal is moving')

class Swimming(Animal):
    def move(self):
        print("swimming")

class Flying(Animal):
    def move(self):
        print('flying')

class Duck(Flying, Swimming):
    def move(self):
        print("duck is swimming and flying")

duck = Duck()
duck.move()
#mro