try:
    1/0
except Exception:
    print('деление на ноль')

while True:
    try:
#        raw = input('Введите число: ')
#        number = int(raw)
        continue
    except ValueError:
        print('Неверный ввод')
    finally:
        break

class Pet:
    pass

class Cat(Pet):
    pass

print(isinstance(Cat(), Cat))