class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}, я родилась {self.birth_date},по профессии {self.occupation}, высшее образование {edu_status}.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Я одноклассник, меня зовут {self.name}, моя группа: {self.group_name}.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Я друг, меня зовут {self.name}, мое хобби: {self.hobby}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наше общее воспоминание: {self.shared_memory}")
person1 = Person(name="Аня", birth_date="15/01/2007", occupation="учитель", higher_education=True)
person1.introduce()
#classmates
classmate1 = Classmate("Бектур", "05.12.2006", "программист", True, "ЕПИ-2")
classmate2 = Classmate("Айбек", "10.02.2007", "дизайнер", False, "ФАДиС-3")
#friends
friend1 = Friend("Алмаз", "15.06.2007", "экономист", True, "Футбол")
friend2 = Friend("Катя", "22.03.2006", "учитель", True, "Рисование")

best_friend = BestFriend("Саша", "01.01.2000", "врач", True, "Путешествия", "Поездка в горы") #лучший друг
people_list = [classmate1, classmate2, friend1, friend2, best_friend]
for person in people_list:
    person.introduce()
