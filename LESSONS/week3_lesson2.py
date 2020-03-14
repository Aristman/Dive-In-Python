class Planet:
    """ Это класс планет"""
    count = 0

    def __new__(cls, *args, **kwargs):
        print('Планета появилась')
        obj = super().__new__(cls)
        return obj

    def __init__(self, name, population=None):
        print('Планета создана')
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __del__(self):
        print('Планета уничтожена')


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
earth = Planet('Земля')
mars = Planet('Марс')
print(Planet.count)
print(earth.__dict__)
earth.mass = 5.97e24
print(earth.__dict__)
print(Planet.__dict__)
print(earth.__class__)
