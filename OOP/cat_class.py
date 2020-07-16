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


    def meow(self):
        return Meow!

class Animal:
    def __init__(self, name, legs, colour):
        self.hunger = 5
        print("I exist")

class Mammal(Animal):
    def __init__(self, name, colour):
        super().__init__(name, 4, colour)

    def give_birth(self):
        print('I have a child')

class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour=colour)

    def wag_tail(self):
        print("wag wag")

class Labrador(Dog):

    def bark(self):
        print("Woolf!")

new_dog = Dog():
    new_dog.