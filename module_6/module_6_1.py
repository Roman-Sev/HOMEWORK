class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Predator(Animal):
    def eat(self,food):
        if food.edible:
            self.fed = True
            print (f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name, edible=True)

cow = Mammal("Корова")
wolf = Predator("Волк")
rose = Plant("Роза")
apple = Fruit("Яблоко")

cow.eat(rose)
cow.eat(apple)
wolf.eat(rose)
wolf.eat(apple)



