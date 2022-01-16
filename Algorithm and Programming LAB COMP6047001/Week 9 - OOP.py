class Animal():
    def __init__(self, species):
        self.species = species
    def print(self):
        print(self.species)

class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Dog')
        self.breed = breed
    def print(self):
        print(self.species)
        print(self.breed)

class Shiba(Dog):
    def __init__(self, name):
        super().__init__('Shiba')
        self.name = name
    def print(self):
        super().print()
        print(self.name)



doggo = Dog('Husky')
doggo.print()
moonmoon = Shiba('moonmoon')
moonmoon.print()