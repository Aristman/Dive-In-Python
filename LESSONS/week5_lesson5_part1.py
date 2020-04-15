class MyIteration:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

def MyGenerator(end):
    current = 0
    while current < end:
        yield current ** 2
        current += 1

def main_prog():
    count = MyIteration(3)
    for now in count:
        print(now)
    for now in MyGenerator(5):
        print(f'Генератор - {now}')


if __name__ == '__main__':
    main_prog()
