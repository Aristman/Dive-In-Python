def grep(pattern):
    print('Старт')
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Стоп')

def under_grep():
    g = grep('python')
    yield from g

def main_prog():
    g = grep('1')
    next(g)
    g.send('1 это выводится')
    g.send('2 не выводится')
    g.close()
    g = under_grep()
    next(g)
    g.send('python is good')
    print(g)
    g.close()


if __name__ == '__main__':
    main_prog()
