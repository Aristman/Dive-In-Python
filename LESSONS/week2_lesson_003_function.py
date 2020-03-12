f = open('input.txt', 'r+')
row = f.read()
print(row)
f.write('1 ,2, 3 ')
f.close()

with open('input.txt') as f:
    print(f.read())
