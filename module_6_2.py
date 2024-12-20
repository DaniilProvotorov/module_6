class Vehicle:

    __COLOR_VARIANTS = ['белый','черный','серый','синий','красный']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color (self):
        return (f'Цвет транспорта: {self.__color}')

    def print_info(self):
        print(f'{Vehicle.get_model(self)} \n{Vehicle.get_horsepower(self)} \n{Vehicle.get_color(self)} \nВладелец: {self.owner}')

    def set_color(self,new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else: print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

v = Sedan('Даниил', 'C3', 300, 'Black')
v.print_info()
v.set_color('голубой')
v.set_color('КРАСНЫЙ')
v.owner = "Denos"
v.print_info()

