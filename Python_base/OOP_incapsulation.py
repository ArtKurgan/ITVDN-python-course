class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    def set_age(self, age):
        if age == 0 or age <= 0:
            self.__age = 'incorrect input'
        else:
            self.__age = age
        return

    def get_age(self):
        return self.__age


student1 = User(5, 'Stepa')

student1.set_age(6)

print(student1.get_age())
