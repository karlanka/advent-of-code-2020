from aoc_utils import get_input, get_input_no_line
import sys
import numpy as np

def one(input):
    """
    >>> one([16,10,15,5,1,11,7,19,6,12,4])
    35
    >>> one([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    220
    """
    input
    input.append(max(input) + 3)
    input.append(0)
    input.sort()
    adap = np.array(input)
    diffs = adap - np.roll(adap,1)
    return np.count_nonzero(diffs == 1) * np.count_nonzero(diffs == 3)

def two(input):
    """ 
    >>> two([1,4,5,6,7,10,11,12,15,16,19])
    8
    #>>> two([28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3])
    #19208
    """
    input.sort()
    print(input)
    # one way to get to 0
    possible_ways = {0: 1}
    
    for adap in input:
        count = 0
        # for each number
        # check how many possible ways there was to get there (max 3 steps back)
        # for possible ones, add that to the number of steps required to get to current 
        for step in [1,2,3]:
            if adap-step in possible_ways:
                count += possible_ways[adap-step]
        possible_ways[adap] = count
        print(adap, possible_ways)

    return(possible_ways[input[-1]])


def main():
    input = get_input(day=10)
    input = list(map(int, input))
    
    print("first:", one(input[:]))
    print("second:", two(input[:]))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()