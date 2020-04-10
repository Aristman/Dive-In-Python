class Descriptor:
    def __get__(self, instance, owner):
        print('get')
        return '1'

    def __set__(self, instance, value):
        print('set')

    def __delete__(self, instance):
        print('delete')


class Value:

    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 100

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = self._prepare_value(value)


class MyClass:
    attr = Descriptor()
    attr1 = Value()

prim1 = MyClass()
prim1.attr = 1
print(prim1.attr)
prim1.attr1 = 20
print(prim1.attr1)