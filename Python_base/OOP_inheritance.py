class Cat:
    def __init__(self, color, cat_type):
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
        else:
            self.size = 'undefined'
        return self.size


class Tiger(Cat):
    def __init__(self, color, cat_type):
        super().__init__(color, cat_type)

    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
        else:
            self.size = 'undefined'
        return self.size


Tyson = Tiger('black', 'wild')

print(Tyson.set_size())
