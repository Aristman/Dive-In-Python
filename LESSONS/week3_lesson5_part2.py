import json
# ------

class PetExport:
    def export(self):
        raise NotImplementedError

class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            'name': dog.name,
            'breed': dog.breed
        })


class ExportXML(PetExport):
    def export(self, dog):
        return f"""<?xml version"1.0" encoding="utf-8"?>
<dog>
    <name>{dog.name}</name>
    <breed>{dog.breed}</breed>
</dog>"""

class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'{self.name} сказал ГАВ'

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed=breed)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError('Bad exporter', exporter)

    def export(self):
        return self._exporter.export(self)


dog = ExDog('Бим', 'Дворняга', exporter=ExportJSON())
print(dog.export())