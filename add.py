"""
Add things
"""

import argparse

def addnum(lhs, rhs):
    if not isinstance(lhs, int):
        raise TypeError('left-hand-side must be int')

    if not isinstance(rhs, int):
        raise TypeError('right-hand-side must be int')
    return lhs + rhs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Add things')
    parser.add_argument('lhs', help = 'Left-hand side')
    parser.add_argument('rhs', help = 'Right-hand-side')

    args = parser.parse_args()

    print(addnum(args.lhs, args.rhs))
