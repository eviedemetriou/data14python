class cats():

    def __init__(self, mood=None, hunger=None, energy=None):
        self.mood = mood
        self.hunger = hunger
        self.energy = energy

    def sleep(self):
        if self.mood == 'happy':
            self.hunger = False
            self.hunger()

    def hunger(self):
        if hunger == True:
            self.energy = 'low'
            meow = self.meow()
            print(f'The cat is {self.energy} on energy. meow')
        elif hunger == False:
            self.energy = 'Medium'

    def energy(self):
        self.energy = input("What is the ")
        if self.energy() == 'low':
            self.hunger = True
        elif self.energy == 'medium':
            self.hunger = False

    def meow(self):
        return "Meow!"

# CLASS INHERITANCE

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.hunger = 5
        print("I exist")

    def breathe(self):
        print("Breathing in...")
        print("Breathing out...")

class Mammal(Animal):
# If we don't include _init_ method then everything from Animal class is inherited
# If we include _init_ then it will overwrite Animal class - Animal attributes will be lost
# Unless we explicitely include attributes of Animal class: super().__init__('all attributes from Animal)
    def __init__(self, name, legs, colour):
        super().__init__(name, legs)
        self.colour = colour

    def give_birth(self):
        print('I have a child')

class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, legs=4, colour=colour)

    def wag_tail(self):
        print("wag wag")
        super().breathe()

class Labrador(Dog):
    # We can overwrite methods and attributes of parent classes by re-writing them with any change we want
    def bark(self):
        print("Woolf!")

my_dog = Dog("Bob", "Brown")
my_dog.wag_tail()

