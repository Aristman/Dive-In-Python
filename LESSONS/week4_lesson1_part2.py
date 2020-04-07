class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

import time


class timer():
    def __init__(self):
        self.time_start = time.time()

    def current_time(self):
        return (time.time()-self.time_start)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Окончание {self.current_time()}')


with timer() as t:
    time.sleep(1)
    print(f'Прошло {t.current_time()}')
    time.sleep(2)
