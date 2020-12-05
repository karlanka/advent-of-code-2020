from aoc_utils import get_input
import sys

def one(input):
    """
    >>> one(['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#'])
    7
    """
    width = len(input[0])
    pos = 0
    hits = 0
    for row in input:
        hits += row[pos] == "#"
        pos += 3
        pos %= width
    return hits

def two(input):
    """
    >>> two(['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#'])
    336
    """
    width = len(input[0])
    tot_hits = 1
    for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        pos = 0
        hits = 0
        for row in input[::down]:
            hits += row[pos] == "#"
            pos += right
            pos %= width
        tot_hits *= hits
    return tot_hits

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