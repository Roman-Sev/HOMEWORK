class Vehicle:
    __COLOR_VARIANTS = ["Black","White","Blue","Red","Green"]
    def __init__(self,owner,model,engine_power,color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        return f"Модель:{self.__model}"
    def get_horsepower(self):
        return f"Мощность двигателя:{self.__engine_power}"
    def get_color(self):
        return f"Цвет:{self.__color}"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец:{self.owner}")

    def set_color(self,new_color):
        if new_color.capitalize() in self.__COLOR_VARIANTS:
            self.__color = new_color.capitalize()
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5


my_car = Sedan(owner="Иван",model="Toyota Camry", engine_power=180,color="Black")
my_car.print_info()

my_car.set_color("Blue")
my_car.print_info()

my_car.set_color("Yellow")
my_car.print_info()

