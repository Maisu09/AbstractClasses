from LandAnimal import LandAnimal

class Cat(LandAnimal):
    __food = str

    def __init__(self, weight: float, name: str, food:str):
        super().__init__(weight, name)
        self.__food = food
    
    @property
    def food(self):
        return self.__food
    
    def feed(self):
        return "The cat feeds with: " + self.__food
    
    def Display(self):
        print("The cat- \n\t" +
                "name: " + self.name + "\n\t" + 
                "weight: " + str(self.weight)+ "\n\t" +
                "food: " + self.__food
        )
