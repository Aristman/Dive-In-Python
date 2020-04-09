from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a ** 2


def main_prog():
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [pool.submit(f, i) for i in range(10)]
        for future in as_completed(results):
            print(future.result())


if __name__ == '__main__':
    main_prog()
