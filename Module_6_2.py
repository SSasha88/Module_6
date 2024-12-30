class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Допустимые цвета
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец может меняться
        self.__model = model  # Модель неизменная
        self.__engine_power = engine_power  # Мощность двигателя неизменная
        self.__color = color  # Цвет может быть изменен только через метод set_color
    def model(self):
        return f"Модель: {self.__model}"
    def horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    def color(self):
        return f"Цвет: {self.__color}"
    def print_info(self):
        print(self.model())
        print(self.horsepower())
        print(self.color())
        print(f"Владелец: {self.owner}")
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Лимит пассажиров для седана
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)
    def get_passengers_limit(self):
        return f"Пассажировместимость: {self.__PASSENGERS_LIMIT}"
    def print_info(self):
        super().print_info()
        print(self.get_passengers_limit())


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print()
# Проверяем что поменялось
vehicle1.print_info()

