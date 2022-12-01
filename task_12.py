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
        return type(self.__calories) in [int, float] and self.__calories < 200

    def is_delicious(self):
        return bool(self.__name)


class JellyBean(Dessert):

    def __init__(self, flavor=None):
        super().__init__()
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, value):
        self.__flavor = value

    def is_delicious(self):
        return self.__flavor != "black licorice"