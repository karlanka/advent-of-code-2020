from aoc_utils import get_input, get_input_no_line
import sys
import itertools
#from operator import sum

def one(input, preamble):
    """
    >>> one([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576], 5)
    127
    """
    for ix, num in enumerate(input):
        if ix > preamble:
            if num not in map(sum, itertools.combinations(input[ix-preamble:ix], 2)):
                return num

def two(input, preamble):
    """
    >>> two([35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576], 5)
    62
    """
    invalid_num = one(input, preamble)
    for ix, num in enumerate(input):
        first_ix = ix
        while num <= invalid_num:
            ix += 1
            num += input[ix]
            if num == invalid_num:
                return min(input[first_ix:ix]) + max(input[first_ix:ix])


def main():
    input = list(map(int, get_input(day=9)))
    preamble = 25

    print("first:", one(input, preamble))
    print("second:", two(input, preamble))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()