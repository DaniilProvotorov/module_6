class Animal:
    alive = True #живой
    fed = False #накормленный
    def __init__(self, name):
        self.name = name


class Plant:
    edible = False
    def __init__(self, name1):
        self.name1 = name1


class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            Mammal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Mammal.alive = False
        if self.fed == True:
            print(f'{self.name} сытый и остался живой')
        else: print(f'{self.name} голодный и погиб')


class Predator(Animal):
    def __init__(self, name):
        self.name = name


    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            Predator.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Predator.alive = False
        if self.fed == True:
            print(f'{self.name} сытый и остался живой')
        else: print(f'{self.name} голодный и погиб')

class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

p1 = Flower('Цветок')
p2 = Fruit('Яблоко')
a1 = Predator('Волк')
a2 = Mammal('Кит')
print(a1.name)
print(a2.name)
a1.eat(p2)
a2.eat(p1)





