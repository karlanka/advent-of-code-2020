from aoc_utils import get_input, get_input_no_line
import sys
import time

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
    
    start = time.time()
    print("first:", one(input))
    print('It took', time.time() - start, 'seconds for first.')
    
    start = time.time()
    print("second:", two(input))
    print('It took', time.time() - start, 'seconds for second.')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()