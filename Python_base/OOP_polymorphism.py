class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type != 'superuser':
            return 'access denied'
        else:
            return 'access granted'


class SuperUser(User):
    def access_database(self):
        return 'access granted'

Artem = User(27, 'Artem', 'superuser')
Karmak = SuperUser(55, 'Karmak', 'supers')

print(Artem.access_database(), '\n' ,Karmak.access_database())