from random import randint

numbers = []
numbers_count = randint(10, 15)
for _ in range(numbers_count):
    numbers.append(randint(1, 100))
print(numbers)
numbers.sort()
print(numbers)
half_len = len(numbers) // 2
mediana = 0
if numbers_count % 2 == 1:
    mediana = numbers[half_len]
else:
    mediana = sum(numbers[half_len-1:half_len + 1]) / 2
print(mediana)

from statistics import median

print(median(numbers))