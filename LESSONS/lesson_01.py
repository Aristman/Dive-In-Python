# Комментарий
print('Hello')
num = 23
print(type(num))
complex_num = 3 - 1j
print(type(complex_num))
print(complex_num.imag)
print(complex_num.real)
# дополнительно изучить документацию на два модуля decimal и fraction
# Есть стандартная библиотека calendar. Для работы с датами и годами

import calendar

print(calendar.leapdays(2000, 2020))
print(*calendar.day_name)
print(calendar.HTMLCalendar())

text1 = """Текск в тройных кавычках будет записан как 
текст на разных строках
    И с абзацами
"""
print(text1)

string1 = 'text'
print(string1.capitalize())  # делает первыю букву в строке заглавной

# Форматирование строк

string2 = '%s простой пример %s текста'
print(string2 % ('Это', 'форматированного'))

# доки на https://docs.python.org/3/library/string.html#format-specification-mini-language

# f строки

vol1 = (1975, 1978)
vol2 = ('Сергей', 'Дима')
for i in range(2):
    print(f'{vol2[i]} родился в {vol1[i]} году')
# К строкам в форматировании применяются модификаторы
# https://docs.python.org/3/library/string.html

string3 = 'Привет'
encode_str = string3.encode(encoding='utf-8')
print(encode_str, type(encode_str))
decode_str = encode_str.decode()
print(decode_str)

pin = False
for i in range(10):
    pin = False if pin else True
    print(pin)

import random
q_num = random.randint(1,100)
while True:
    in_num = input('Введите число:')
    if not in_num or in_num == 'exit':
        break
    if not in_num.isdigit():
        print('Неверный ввод. Введите число')
        continue
    in_num = int(in_num)
    if in_num > q_num:
        print('Загаданное число меньше')
    elif in_num < q_num:
        print('Загаданное число больше')
    else:
        print('Совершенно верно!')
        break
