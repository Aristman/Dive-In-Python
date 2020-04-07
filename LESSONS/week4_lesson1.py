class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        return {
            'name': self.name,
            'email': self.email
        }

    def __str__(self):
        return f'{self.name} <{self.email}>'

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email


#    def __getattribute__(self, item):
#        return 'Атрибут для объекта'

class Reseacher:
    def __getattr__(self, item):
        return f'Нет такого атрибута у класса \n'

    def __getattribute__(self, item):
        print(f'Ищем атрибут {item}')
        return object.__getattribute__(self, item)

    def __getitem__(self, item):
        print(f'значение ключа {item} равно ')

    def __setitem__(self, key, value):
        print(f'Просвоено {key} зачение {value}')


serg = User('Сергей', 'serg@mars-lab.ru')
natasha = User('Наташа', 'serg@mars-lab.ru')
print(serg.get_email())
print(serg)
print(serg == natasha)
print(hash(serg))
print(hash(natasha))

obj = Reseacher()
print(obj.attr1)
obj.attr1 = 10
print(obj.attr1)
obj['first'] = 10
print(obj['firs'])
print('-------------------------')

it = iter((1, 3, 5, 7))
print(next(it))
print(next(it))
print('-----------------------')


class SquareIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        res = self.current ** 2
        self.current += 1
        return res


for i in SquareIter(1, 6):
    print(i)
