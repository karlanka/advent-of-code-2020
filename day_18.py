from aoc_utils import get_input, get_input_no_line
import sys
import re
import time

def calculator(expression):
    """
    >>> calculator('1 + 2 * 3 + 4 * 5 + 6')
    71
    >>> calculator('1 + 2 * 30')
    90
    >>> calculator('7*3*3+9*3+56')
    272
    """
    expression = expression.replace(' ','')
    numbers = list(map(int, re.findall(r'\d+', expression)))
    if len(numbers) == 0:
        return numbers[0]
    operators = list(re.findall(r'\D+', expression))
    ix = 0
    tot = numbers[0]
    
    while ix < len(operators):
        if operators[ix] == '+':
            tot += numbers[ix + 1]
        elif operators[ix] == '*':
            tot *= numbers[ix + 1]
        ix += 1

    return tot

def parser_one(expression):
    """
    >>> parser_one('2 * 3 + (4 * 5)')
    26
    >>> parser_one('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    437
    >>> parser_one('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    12240
    """
    expression = expression.replace(' ','')

    if '(' not in expression:
        return calculator(expression)
    
    hit = 0
    for ix, val in enumerate(expression):
        if val == '(':
            hit = ix
        elif val == ')':
            par_value = calculator(expression[hit+1:ix])
            break
    expression = expression[:hit] + str(par_value) + expression[ix+1:]
    
    return parser_one(expression)
    
def advanced_calculator(expression):
    """
    >>> advanced_calculator('1 + 2 * 3')
    9
    >>> advanced_calculator('1 * 2 + 3')
    5
    >>> advanced_calculator('1 * 2 + 3 * 3 + 2')
    25
    """
    expression = expression.replace(' ','')
    if '+' not in expression:
        return eval(expression)
    for ix, val in enumerate(expression):
        if val == '+':
            a = list(re.findall(r'\d+', expression[:ix]))[-1]
            b = list(re.findall(r'\d+', expression[ix:]))[0]
            x = int(a) + int(b)
            expression = expression[:ix-len(a)] + str(x) + expression[ix+len(b)+1:]
            break
    
    return advanced_calculator(expression)

def parser_two(expression):
    """
    >>> parser_two('1 + (2 * 3) + (4 * (5 + 6))')
    51
    >>> parser_two('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    669060
    """
    expression = expression.replace(' ','')

    if '(' not in expression:
        return advanced_calculator(expression)
    
    hit = 0
    for ix, val in enumerate(expression):
        if val == '(':
            hit = ix
        elif val == ')':
            par_value = advanced_calculator(expression[hit+1:ix])
            break
    expression = expression[:hit] + str(par_value) + expression[ix+1:]
    
    return parser_two(expression)
    

def one(input):
    tot = 0
    for row in input:
        tot += parser_one(row)
    return tot

def two(input):
    tot = 0
    for row in input:
        tot += parser_two(row)
    return tot


def main():
    input = get_input(day=18)
    
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