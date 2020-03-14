class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        return text

    def say_name(self):
        return self._say(f'Я - {self._name}')

    def say_how_old(self):
        return self._say(f'Мне {self._age} лет')


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human: Human):
        print(f'Добро пожаловать на {self.name}, {human._name}!')
        self.population.append(human)

mars = Planet('Марс')
serg = Human('Сергей', age=44)
print(serg.say_name())
print(serg.say_how_old())
mars.add_human(serg)
print(mars.population)
print(mars.population[0].say_name())