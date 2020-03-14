def gen_range(start, end):
    current = start
    while current < end:
        yield current
        print('Текущие значение {}'.format(current))
        current += 1

x = gen_range(2,5)
print(next(x))
print(next(x))
print(next(x))

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Передано: {}'.format(value))
        if not value: break
        total += value

gen = accumulator()
next(gen)
print(gen.send(10))
print(gen.send(20))