from abc import ABC, abstractclassmethod
from Animal import Animal

class LandAnimal(Animal, ABC):

    #overloading abstract method

    def breath(self):
        print("The land animal can breath only on the land.")

    def walk(self):
        print("The land animal can walk and swim.")
    
    