from aoc_utils import get_input, get_input_no_line
import sys

def one(input):
    """
    >>> one([['abc'],['a','b','c'],['ab','ac'],['a','a','a','a'],['b']])
    11
    """
    return sum((len(set(list(x))) for x in (''.join(x) for x in input)))

def two(input):
    """
    >>> two([['abc'],['a','b','c'],['ab','ac'],['a','a','a','a'],['b']])
    6
    """
    total = 0
    for answers in input:
        total += len(set.intersection(*(set(x) for x in (answers))))
    return total

def main():
    input = [x.split('\n') for x in get_input_no_line(day=6).split('\n\n')]

    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()