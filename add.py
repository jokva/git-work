"""
Add things
"""

import argparse

def addnum(x, y):
    return x + y

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Add things')
    parser.add_argument('lhs', help = 'Left-hand side')
    parser.add_argument('rhs', help = 'Right-hand-side')

    args = parser.parse_args()

    print(addnum(args.lhs, args.rhs))
