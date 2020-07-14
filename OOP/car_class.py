class Car:

    def __init__(self, colour, make, speed):
        self.type = 'petrol engine'
        self.colour = colour
        self.make = make
        self.speed = speed

    def get_speed(self):
        return self.speed

    def accel_speed(self, accel):
        self.speed = self.speed * accel
        if self.speed > 200:
            self.speed = 200

    def braking_speed(self, decel):
        self.speed = self.speed * decel
        if self.speed < 0:
            self.speed = 0

F1 = Car('red', 'ferrari', 60)
print(F1.type, F1.colour, F1.make, F1.speed, '\n')

F1.accel_speed(3.5)
print(F1.get_speed())
F1.braking_speed(0)
print(F1.get_speed())
if F1.get_speed() > 0:
    print(f'You are moving at {F1.get_speed()}mph')
else:
    print(f'You are stationary')