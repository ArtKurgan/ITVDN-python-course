class Database:
    def __init__(self):
        self.data_list = []

    def read_data(self, criteria):
        result = []
        for object in self.data_list:
            matches = 0
            for key, value in criteria.items():
                if object.__dict__.get(key) == value:
                    matches += 1
                if matches == len(criteria):
                    result.append(object.return_list())
        if len(result) != 0:
            return print(result)
        else:
            print('No data found!')

    def write_data(self, element):
        self.data_list.append(element)


class Data:
    def __init__(self, country, name, age):
        self.country = country
        self.name = name
        self.age = age

    def return_list(self):
        return [self.country, self.name, self.age]


data = Database()
chel = Data('Ukraine', 'Valera', 20)
chel2 = Data('Poland', 'Anton', 31)
chel3 = Data('Poland', 'Pwek', 20)

data.write_data(chel)
data.write_data(chel2)
data.write_data(chel3)

find1 = {'country': 'Poland', 'age': 20}
data.read_data(find1)
