from aoc_utils import get_input, get_input_no_line
import sys

def decoder(boarding_pass):
    """
    >>> decoder('FBFBBFFRLR')
    357
    >>> decoder('BFFFBBFRRR')
    567
    >>> decoder('FFFBBBFRRR')
    119
    >>> decoder('BBFFBBFRLL')
    820
    """
    boarding_pass = boarding_pass.replace('B','1').replace('R','1').replace('F','0').replace('L','0')
    return int(boarding_pass, 2)


def one(input):
    return max((decoder(x) for x in input))

def two(input):
    id_set = set([decoder(x) for x in input])
    id_tot = set(range(min(id_set), max(id_set)+1))
    return id_tot - id_set

def main():
    input = get_input(day=5)
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()