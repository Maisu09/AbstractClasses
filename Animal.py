from abc import ABC, abstractmethod

class Animal(ABC):
    __weight = float()
    __name  = str()

    def __init__(self, weight:float, name:str):
        self.__weight = weight
        self.__name = name

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def feed(self, food:str):
        pass

    @abstractmethod
    def breath(self):
        pass


    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight:float):
        self.__weight - weight
        self.__init__(self.__weight, self.__name)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name
        self.__init__(self.__weight, self.__name)
    



