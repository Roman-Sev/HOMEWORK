import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive: ")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f"X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, i'm dangerous")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        egg_count = random.randint(1, 4)
        print(F"Here are(is) {egg_count} egg(s) for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz_adjusted = abs(dz)/2 * self.speed
        new_z = self._cords[2] - dz_adjusted
        if new_z < 0:
            print("It's too deep, i can't dive: ")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird,AquaticAnimal,PoisonousAnimal):
    sound = "Click-click-click"

duckbill = Duckbill(speed=2)
duckbill.get_cords()
duckbill.move(1,1,0)
duckbill.lay_eggs()
duckbill.attack()









