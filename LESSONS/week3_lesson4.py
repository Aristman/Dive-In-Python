class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 120


class Robot:

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('Робот бесполезен')
        del self._power


myRobot = Robot(100)
myRobot.power = 2000
newRobot = Robot(200)
newRobot.power = -10
print(newRobot.power)
del newRobot.power
