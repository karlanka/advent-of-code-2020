from aoc_utils import get_input, get_input_no_line
import sys
import itertools
import collections

def close_adjacent(seat, row_len, col_len):
    adjacent_list = []
    seat_x, seat_y = seat
    for x, y in itertools.product((-1,0,1), (-1,0,1)):
        adj_seat = (seat_x + x, seat_y + y)
        if adj_seat == seat or adj_seat[0] < 0 or adj_seat[1] < 0 or adj_seat[0] >= row_len or adj_seat[1] >= col_len:
            continue
        adjacent_list.append(adj_seat)
    return adjacent_list
    
def one(input):
    """
    >>> one(['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL'])
    37
    """
    ferry = []
    for rows in input:
        ferry.append(list(rows))

    n_rows, n_cols = len(input), len(input[1])

    while True:
        to_change = {}
        for row_ix, row in enumerate(ferry):
            for col_ix, col in enumerate(row):
                taken = 0
                if col == '.':
                    continue
                for x, y in close_adjacent((row_ix, col_ix), n_rows, n_cols):
                    taken += ferry[x][y] == '#'
                if taken >= 4 and col == '#':
                    to_change[(row_ix, col_ix)] = "L"
                if taken == 0 and col == 'L':
                    to_change[(row_ix, col_ix)] = "#"
        if not to_change:
            break
        for (x,y), v in to_change.items():
            ferry[x][y] = v
    
    return collections.Counter([x for y in ferry for x in y])['#']

def all_adjacents(pos, n_rows, n_cols):
    r, c = pos
    adjacent_list = [
        [(r, c+x) for x in range(1, n_cols-c)], # right
        [(r, c-x) for x in range(1, c+1)], # left
        [(r-x, c) for x in range(1, r+1)], # up
        [(r+x, c) for x in range(1, n_rows-r)], # down
        [(r-x, c-x) for x in range(1, min(r+1, c+1))], # left up
        [(r+x, c-x) for x in range(1, min(n_rows-r, c+1))], # left down
        [(r+x, c+x) for x in range(1, min(n_rows-r, n_cols-c))], # right down
        [(r-x, c+x) for x in range(1, min(r+1, n_cols-c))] # right up
    ]
    return adjacent_list

def two(input):
    """
    >>> two(['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL'])
    26
    """
    ferry = []
    for rows in input:
        ferry.append(list(rows))

    n_rows, n_cols = len(input), len(input[1])

    while True:
        to_change = {}
        for row_ix, row in enumerate(ferry):
            for col_ix, col in enumerate(row):
                taken = 0
                if col == '.':
                    continue
                for adjacent in all_adjacents((row_ix, col_ix), n_rows, n_cols):
                    for x, y in adjacent:
                        if ferry[x][y] == 'L':
                            break
                        if ferry[x][y] == '#':
                            taken += 1
                            break
                if taken >= 5 and col == '#':
                    to_change[(row_ix, col_ix)] = 'L'
                if taken == 0 and col == 'L':
                    to_change[(row_ix, col_ix)] = '#'

        if not to_change:
            break

        for (x,y), v in to_change.items():
            ferry[x][y] = v
        
    return collections.Counter([x for y in ferry for x in y])['#']

def main():
    input = get_input(day=11)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()