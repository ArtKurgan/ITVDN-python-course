class Database:
    def __init__(self):
        self.data_list = []
        self.Data = Data

    def read_data(self, criteria):
        result = []
        for object in self.data_list:
            if object.__dict__.get(list(criteria.keys())[0]) == list(criteria.values())[0]:
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
chel3 = Data('Poland', 'Pwek', 22)

data.write_data(chel)
data.write_data(chel2)
data.write_data(chel3)

find1 = {'country': 'Poland'}
data.read_data(find1)
