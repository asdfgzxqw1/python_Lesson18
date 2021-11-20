class Animal:
    def __init__(self, name, age):
        self.attriburts = {'name': name, 'age': age}

    def eat(self, _amout=0):
        print("Ate some food")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, amout=0.1):
        if amout > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def aet(self, _amout=0):
        print("Ate some dog food!")


pluta = Dog('Pluta', 3)
goofy = Dog('Goofy', 2)
buttons = Cat('Mr.Buttons', 4)

animals = (pluta, goofy, buttons)

for animal in animals:
    if animal.attriburts['age'] > 2:
        print(animal.attriburts['name'])

# перезаписали все по принципу interface segregation принцип которого заклчается в том что много интерфейсов
# специально предназначенных для клиентов лучше чем один интерфейс общего назначения клиент не должен включать

