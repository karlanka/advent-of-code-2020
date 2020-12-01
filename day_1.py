from aoc_utils import get_input
import sys

def one(input):
    """
    >>> one([1721,979,366,299,675,1456])
    514579
    """
    input = sorted(input)
    for x in input:
        if 2020 - x in input:
            return x * (2020-x)

def two(input):
    """
    >>> two([1721,979,366,299,675,1456])
    241861950
    """
    input = sorted(input)
    for i, x in enumerate(input):
        goal = 2020 - x
        for y in input[i:]:
            if goal - y in input:
                return (2020 - x - y) * x * y

            

def main():
    input = list(map(int, get_input(day=1)))
    print("first:", one(input))
    print("second:", two(input))
    print(sorted(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()