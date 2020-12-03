from aoc_utils import get_input
import sys
import math

def one(input):
    """
    >>> one(['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#'])
    7
    """
    width = len(input[0])
    pos = 0
    hits = 0
    for row in input:
       if row[pos] == "#":
           hits += 1
       pos += 3
       pos %= width
    return hits

def two(input):
    """
    >>> two(['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#'])
    336
    """
    width = len(input[0])
    hits_list = []
    for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        pos = 0
        hits = 0
        for row in input[::down]:
            if row[pos] == "#":
                hits += 1
            pos += right
            pos %= width
        hits_list.append(hits)

    return math.prod(hits_list)

def main():
    input = get_input(day=3)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()