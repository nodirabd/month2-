class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        if self.higher_education == True :
            education_status = "есть"
        else:
            education_status = "нет"
        print(f"Меня зовут {self.name}, я родился(лась) {self.birth_date},по профессии {self.occupation}, высшее образование {education_status}.")
person1 = Person(name="Аня", birth_date="15/01/2002", occupation="учитель", higher_education=True)
person2 = Person(name="Таня", birth_date="20/05/1995", occupation="программист", higher_education=True)
person3 = Person(name="Анна", birth_date="10/11/2005", occupation="студент", higher_education=False)
person1.introduce()
person2.introduce()
person3.introduce()
