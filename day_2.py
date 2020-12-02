from aoc_utils import get_input
import sys
import collections

def one(input):
    """
    >>> one(['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc'])
    2
    """
    valid = 0
    for rule_pw in input:
        limits, letter, pw = rule_pw.split(' ')
        lower, upper = map(int, limits.split('-'))
        counter = collections.Counter(pw)
        if lower <= counter[letter[0]] <= upper:
            valid += 1
    return valid

def two(input):
    """
    >>> two(['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc'])
    1
    """
    valid = 0
    for rule_pw in input:
        limits, letter, pw = rule_pw.split(' ')
        lower, upper = map(int, limits.split('-'))
        if bool(pw[lower-1] == letter[0]) ^ bool(pw[upper-1] == letter[0]):
            valid += 1
    return valid

def main():
    input = get_input(day=2)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()