from Animal import Animal
from AquaticAnimal import AquaticAnimal
from Cat import Cat
from Fish import Fish

def main():
    fish = Fish(5, "Nemo", "worm")
    print(fish.feed())
    fish.breath()
    fish.walk()
    fish.Display()

    print("\n")

    cat = Cat(5, "Tom", "fish")
    print(cat.feed())
    cat.breath()
    cat.walk()
    cat.Display()




if __name__ == '__main__':
    main()