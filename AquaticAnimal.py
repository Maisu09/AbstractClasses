from abc import ABC
from Animal import Animal


class AquaticAnimal(Animal, ABC):
    
    #overriding abstract method
    def breath(self):
        print("The aquatic animals can breath underwater.")

    #overriding abstract method
    def walk(self):
        print("The aquatic animals swim.")

