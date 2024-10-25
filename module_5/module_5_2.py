class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
                print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"

house = House("ЖК ЭЛЬБРУС", 30)
print(len(house))
print(house)
