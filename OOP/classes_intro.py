class Dog:

    # INITIALIZATION - the things that happen automatically on INSTANTIATION
    def __init__(self, name='Pablo'):  # Can have default object names like with regular functions
        self.name = name
        self.animal_kind = 'canine'
        self.legs = 4
        self._secret = 'I can\'t eat chocolate'  # PRIVATE VARIABLES
# _secret hides attribute from IDE
# __secret hides attribute entirely but can use it inside a class

    def say_name(self):
        return f'My name is {self.name}'

    def get_secret(self):  # GETTER
        return self._secret

    def set_secret(self, secret):  #SETTER
        self._secret = secret


big_dog = Dog()  # INSTANTIATION - creating an instance of a class
print(big_dog.name)
big_dog.name = 'Collin'  # Can change initial attribute (Fluffy -> Collin)
print(big_dog.name)
print('\n')

# Changing Dog's attribute won't make a change in class objects - have to change individual objects if needed
Dog.animal_kind = 'Arachnid'
Dog.legs = 8
small_dog = Dog('Lucy')
print(type(small_dog))
print(small_dog.animal_kind)
print(small_dog.legs)
print('\n')

# Calling class methods requires () - not brackets for attributes
new_dog = Dog('Lassie')
print(new_dog._secret)
print(new_dog.say_name())
print('\n')

# Changing an attribute in the class - for specific object - using SETTER and GETTER methods
print(new_dog.get_secret())
new_dog.set_secret('I hid my bone in the garden')  # set_secret does something rather than return something - so no 'print'
print(new_dog.get_secret())  # get_secret will give then new secret set


