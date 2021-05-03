from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return

    @abstractmethod
    def consumption_cloth(*args):
        return sum([i.consumption_cloth for i in args])


class Coat(Clothes):
    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 30:
            self.__param = 30
        elif param > 70:
            self.__param = 70
        else:
            self.__param = param

    @property
    def consumption_cloth(self):
        return self.param / 6.5 + 0.5


class Costume(Clothes):
    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 1.1:
            self.__param = 1.1
        elif param > 2.4:
            self.__param = 2.4
        else:
            self.__param = param

    @property
    def consumption_cloth(self):
        return self.param * 2 + 0.3


coat_1 = Coat(30)
coat_2 = Coat(26)
costume_1 = Costume(2.4)
costume_2 = Costume(2.7)
print(coat_1.consumption_cloth)
print(coat_2.consumption_cloth)
print(costume_1.consumption_cloth)
print(costume_2.consumption_cloth)
print(Clothes.consumption_cloth(coat_1, costume_1, coat_2))
