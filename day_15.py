from aoc_utils import get_input, get_input_no_line
import sys


def one_and_two(input, steps):
    """
    >>> one_and_two([0,3,6], 2020)
    436
    """
    spoken = {x: i for i, x in enumerate(input)}

    prev = input[-1]
    for ix in range(len(input), steps):
        if prev in spoken:
            speaks = ix - spoken[prev] - 1
        else:
            speaks = 0
        spoken[prev] = ix - 1
        prev = speaks
    return prev

def main():
    input = [0,14,6,20,1,4]
    
    print("first:", one_and_two(input,2020))
    print("second:", one_and_two(input, 30000000))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()