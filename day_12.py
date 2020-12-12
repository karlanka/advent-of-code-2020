from aoc_utils import get_input, get_input_no_line
import sys

def one(input):
    """
    >>> one(['F10','N3','F7','R90','F11'])
    25
    """
    directions = [(1,0), (0,-1), (-1,0), (0,1)] 
    cur_dir = 0
    pos = (0,0)
    for ins, val in [(x[0], int(x[1:])) for x in input]:
        if ins == 'F':
            pos = (pos[0] + directions[cur_dir][0] * val, pos[1] + directions[cur_dir][1] * val)
        elif ins == 'N':
            pos = (pos[0], pos[1] + val)
        elif ins == 'S':
            pos = (pos[0], pos[1] - val)
        elif ins == 'E':
            pos = (pos[0] + val, pos[1])
        elif ins == 'W':
            pos = (pos[0] - val, pos[1])
        elif ins == 'R':
            cur_dir += (val // 90)
        elif ins == 'L':
            cur_dir -= (val // 90)
        cur_dir %= 4

    return (abs(pos[0])+abs(pos[1]))

def two(input):
    """
    >>> two(['F10','N3','F7','R90','F11'])
    286
    """
    ship_pos = (0,0)
    wp_pos = (10,1)
    for ins, val in [(x[0], int(x[1:])) for x in input]:
        if ins == 'N':
            wp_pos = (wp_pos[0], wp_pos[1] + val)
        elif ins == 'S':
            wp_pos = (wp_pos[0], wp_pos[1] - val)
        elif ins == 'W':
            wp_pos = (wp_pos[0] - val, wp_pos[1])
        elif ins == 'E':
            wp_pos = (wp_pos[0] + val, wp_pos[1])
        elif ins == 'F':
            ship_pos = (ship_pos[0] + wp_pos[0] * val, ship_pos[1] + wp_pos[1] * val)
        elif val == 180:
            wp_pos = (-1 * wp_pos[0], -1 * wp_pos[1])
        elif (val == 90 and ins == 'R') or (val == 270 and ins == 'L'):
            wp_pos = (wp_pos[1], -1 * wp_pos[0])
        elif (val == 270 and ins == 'R') or (val == 90 and ins == 'L'):
            wp_pos = (-1 * wp_pos[1], wp_pos[0])

    return (abs(ship_pos[0])+abs(ship_pos[1]))

def main():
    input = get_input(day=12)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()
