import sys

count_steps = int(sys.argv[1])
for i in range(1, count_steps + 1):
    print(' ' * (count_steps - i) + '#' * i)
