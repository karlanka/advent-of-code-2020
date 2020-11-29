from aoc_utils import get_input
import sys

def one(input):
    """
    >>> one()
    """
    return

def two(input):
    """
    >>> two()
    """
    return

def main():
    input = get_input(day=0)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()