# http://www.reddit.com/r/dailyprogrammer/comments/22k8hu/492014_challenge_157_intermediate_puzzle_cube/

from sys import argv

def load_move_list(filename):
    return list(open(filename).read().split())


def build_cube(size):
    if int(size) == 3:
        cube = {
            'D' : [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
            'U' : [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
            'L' : [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
            'R' : [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
            'F' : [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
            'B' : [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        }
    else:
        print('Size %s is not supported at this time.' % size)
        exit(0)

    return cube


def cube_rotate(cube, side):
    if side in ['L', 'R', 'F', 'B']:
        print('spin %r 90c' % side)
    else:
        print('tilt %r 90c' % side)

    return cube


def print_side(side):
    print('\n'.join([''.join([square for square in row]) for row in side]))


def main(size, move_list):
    cube = build_cube(size)

    for move in move_list:
        if len(move) > 1:
            if move[1] == "'":
                cube = cube_rotate(cube, move[0])
                cube = cube_rotate(cube, move[0])
                cube = cube_rotate(cube, move[0])
            else:
                cube = cube_rotate(cube, move[0])
                cube = cube_rotate(cube, move[0])
        else:
            cube = cube_rotate(cube, move[0])

    print_side(cube['F'])


if __name__ == "__main__":
    main(argv[1], load_move_list(argv[2]))
