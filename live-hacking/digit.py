import sys

table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

try:
    print(table[int(sys.argv[1])])
except ValueError:
    print(sys.argv[1], 'is not an integer')
except KeyError:
    print(sys.argv[1], 'is not a digit')
