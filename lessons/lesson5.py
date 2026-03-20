class User:
    #переменные класса
    user_count = 0
    default_password = "12345678"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.password = User.default_password

    #@classmethod
#экхемпляр=объект

user_1 = User("Игорь", "996555000001")
user_2 = User("Курманбек", "996555000002")
print(user_1.name)
print(user_2.name)
print(user_1.password, user_2.password)
User.user_count += 1

print(f'Количество юзеров {User.user_count}')
#branch = vetka
