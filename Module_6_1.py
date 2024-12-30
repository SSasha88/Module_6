class Animal:
    def __init__(self, name):
        self.alive = True # (живой)
        self.fed = False # (накормленный)
        self.name = name #  индивидуальное название каждого животного.

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Plant:
    def __init__(self, name):
        self.edible = False # (съедобность)
        self.name = name #  индивидуальное название каждого растения

# 4 класса наследника:
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        # Переопределяем значение атрибута edible для фруктов
        self.edible = True

# объекты животных и растений
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод имени
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверка начального состояния
print(a1.alive)  # True
print(a2.fed)    # False

# Хищник пытается съесть цветок
a1.eat(p1)
# Волк с Уолл-Стрит не стал есть Цветик семицветик

# Млекопитающее ест фрукт
a2.eat(p2)
# Хатико съел Заводной апельсин

# Проверка новых состояний
print(a1.alive)  # False
print(a2.fed)    # True
