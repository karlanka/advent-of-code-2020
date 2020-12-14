from aoc_utils import get_input, get_input_no_line
import sys
import operator
import time

def one(input):
    """
    >>> one(['939', '7,13,x,x,59,x,31,19'])
    295
    """
    arrival = int(input[0])
    buses = [int(x) for x in input[1].split(',') if x.isdigit()]
    depart = [((arrival // bus) + 1) * bus - arrival for bus in buses]
    return buses[depart.index(min(depart))] * min(depart)


def two(input):
    """
    >>> two('7,13,x,x,59,x,31,19')
    1068781
    >>> two('67,7,59,61')
    754018
    >>> two('17,x,13,19')
    3417
    >>> two('67,7,x,59,61')
    1261476
    >>> two('1789,37,47,1889')
    1202161486
    >>> two('1789,37,47,1889')
    1202161486
    """
    buses = [(i, int(x)) for i,x in enumerate(input.split(',')) if x.isdigit()]
    loop_incr = buses[0][1]
    t = 0
    for t_diff, bus in buses[1:]: 
        while True:
            if (t + t_diff) % bus == 0:
                break 
            t += loop_incr
        loop_incr *= bus
    return t

def main():
    input = get_input(day=13)
    
    print("first:", one(input))
    print("second:", two(input[1]))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()