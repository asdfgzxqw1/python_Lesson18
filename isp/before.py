class Creature:
    def __init__(self, name):
        self.name = name

    def swim(self):
        pass

    def walk(self):
        pass

    def talk(self):
        pass


class Human(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"i'm {self.name} and i can swim")

    def walk(self):
        print(f"i'm {self.name} and i can walk")

    def talk(self):
        print(f"i'm {self.name} and i can walk")


class Fish(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"i'm {self.name} and i can swim")


class Cat(Creature):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"i'm {self.name} and i can swin")

    def walk(self):
        print(f"i'm {self.name} and i can walk")


humen = Human("John Doe")
humen.swim()
humen.walk()
humen.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("Mr.Buttons")
cat.walk()
cat.swim()
cat.talk()
