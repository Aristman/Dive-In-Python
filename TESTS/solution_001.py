import sys

in_string = sys.argv[1]
result = 0
for i in in_string:
    result += int(i)
print(result)
