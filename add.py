"""
Add things

Things includes numbers and lists
"""

import argparse

def addnum(lhs, rhs):
    if not float(lhs).is_integer():
        raise TypeError('left-hand-side must be int')

    if not float(rhs).is_integer():
        raise TypeError('right-hand-side must be int')
    return lhs + rhs

def addlist(x, y):
    return [x] + y

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Add things')
    parser.add_argument('lhs', help = 'Left-hand side')
    parser.add_argument('rhs', help = 'Right-hand-side')
    parser.add_argument('tail', type = int, nargs = '*', help = 'More')

    args = parser.parse_args()

    out = addnum(args.lhs, args.rhs)
    if args.tail:
        out = addlist(out, args.tail)

    print(out)
