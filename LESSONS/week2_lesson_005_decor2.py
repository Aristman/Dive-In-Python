

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'r+') as f:
                f.readlines()
                f.write(str(result))
                f.write('\n----------\n')

        return wrapped

    return decorator


@logger('new_log.txt')
def squart(num_list):
    return list(map(lambda x: x**2, num_list))


squart(range(10))
