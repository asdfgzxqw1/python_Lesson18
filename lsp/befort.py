class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print("Ate some food!")


class Cat(Animal):
    def eat(self, amunt=0.1):
        if amunt > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def aet(self):
        print("Ate some dog food!")


pluta = Dog({'name': 'Pluta', 'age': 3})
goofy = Dog({'name': 'Goofy', 'age': 2})
buttons = Cat(('Mr.Buttons', 4))

animals = (pluta, goofy, buttons)

for animals in animals:
    if animals.attributes['age'] > 2:
        print(animals.attributes['name'])
