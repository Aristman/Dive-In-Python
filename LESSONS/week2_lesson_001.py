from random import randint

my_list = ['один', 'два', 'три', 'четыре', 'пять']
for x, y in (enumerate(my_list, 1)):
    print('{} это элемент номер {}'.format(y, x))

numbers = []
for _ in range(10):
    numbers.append(randint(1, 100))
print(numbers)
print(sorted(numbers), numbers)
numbers.sort(reverse=True)
print(numbers)
