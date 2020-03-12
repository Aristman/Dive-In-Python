def get_multy(arg1):
    def inner(arg2):
        return arg2 * arg1

    return inner


mul_2 = get_multy(2)
print(mul_2(12))

print(list(filter(lambda x: x > 0, range(-3, 6))))


def list_numTostr(mylist):
    return list(map(str, mylist))


print(list_numTostr(range(10)))

squar_list = [num ** 2 for num in range(20)]
print(squar_list)
print(len(squar_list))

squar_even_list = [num for num in range(10) if num % 3 == 0]
print(squar_even_list)

square_set = {num: num ** 2 for num in range(15)}
print(square_set)

