beatles_men = {
    'Пол Маккартни': 'Бас-гитара',
    'Джон Леннон': 'Ритм-гитара',
    'Джорж Майкл': 'Ритм-гитара'
}
print(beatles_men)
beatles_men['Ринго Стар'] = 'Барабаны'
print(beatles_men)
del beatles_men['Джон Леннон']
print(beatles_men)
beatles_men.update({
    'Джон Леннон': 'Ритм-гитара'
})
print(beatles_men)
print(beatles_men.pop('Ринго Стар'))
print(beatles_men)

for man, sound in beatles_men.items():
    print(f'{sound}, на ней играет {man}')

from collections import  OrderedDict
