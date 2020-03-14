class Human:
    pass


class Robot:
    """ Данный клас пустой и ничего не делает"""


print(Robot)
print(dir(Robot))


class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Планета {self.name}'

planet = Planet('Меркурий')
print(planet.name)
print(planet)

planet_names = (
    'Меркурий',
    'Венера',
    'Земля',
    'Марс',
    'Сатурн',
    'Юпитер',
    'Уран',
    'Нептун'
)

solar_system = []
for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)