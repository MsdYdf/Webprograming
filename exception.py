import sys

try:
    x = int(input('X = '))
    y = int(input('Y = '))
except ValueError:
    print('Input must be number.')
    sys.exit(1)


try:
    result = x/y
except ZeroDivisionError:
    print('Can not divided by 0.')
    sys.exit(1)

print(f'{x} / {y} = {result}')