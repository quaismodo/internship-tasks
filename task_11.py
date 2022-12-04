class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value

    def is_healthy(self):
        return isinstance(self.__calories, (int, float)) and self.__calories < 200

    def is_delicious(self):
        return bool(self.__name)


c = Dessert()
print(f'{c.name} - {c.is_delicious()}, {c.calories} - {c.is_healthy()}')
c.name = 'Icecream'
c.calories = 200
print(f'{c.name} - {c.is_delicious()}, {c.calories} - {c.is_healthy()}')
c.calories = 180
print(f'{c.name} - {c.is_delicious()}, {c.calories} - {c.is_healthy()}')
