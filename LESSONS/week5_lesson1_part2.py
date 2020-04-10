from multiprocessing import Process


class Hello(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Hello: {self.name}')
        while True:
            pass


def main_prog():
    p = Hello('serg')
    p.start()
    print(p.pid)
    p.is_alive()
#    p.join()
    s = Hello('Alex')
    s.start()
    print(s.pid)
#    s.join()


if __name__ == '__main__':
    main_prog()
