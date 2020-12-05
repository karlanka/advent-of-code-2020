from aoc_utils import get_input, get_input_no_line
import sys

def one(input):
    """
    >>> one(input)
    """
    return

def two(input):
    """
    >>> two(input)
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