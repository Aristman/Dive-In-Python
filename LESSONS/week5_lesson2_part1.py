from threading import Thread


class HelloThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Привет, {self.name}')


def t(name):
    print(f'Привет, {name}')


def main_prog():
    th = Thread(target=t, args=('Сергей',))
    th.start()
    th.join()


if __name__ == '__main__':
    main_prog()
