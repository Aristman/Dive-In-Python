class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'{self.name} сказал ГАВ'

dog = Dog('Шарик', 'Дворняжка')
print(dog.say())

import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            'name': self.name,
            'breed': self.breed
        })

class ExDog(Dog, ExportJSON):
    pass

ex_dog = ExDog('Бим', 'Дворняга')
print(ex_dog.to_json())