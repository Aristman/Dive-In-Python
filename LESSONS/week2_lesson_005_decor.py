import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(str(result))
            f.write('\n')
        return result

    return wrapped


@logger
def summator(num_list):
    return sum(num_list)

@logger
def getSet():
    return {
        'Пол Маккартни': 'Бас-гитара',
        'Джон Леннон': 'Ритм-гитара',
        'Джорж Майкл': 'Ритм-гитара'
    }

summator(range(6))
getSet()
print(getSet.__name__)
