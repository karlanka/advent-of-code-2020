from aoc_utils import get_input, get_input_no_line
import sys

def computer(instructions):
    acc, pos = 0, 0
    visited = []
    length = len(instructions)
    while True:
        if pos > length - 1:
            return acc, False
        if pos in visited:
            return acc, True
        visited.append(pos)
        inst, val = instructions[pos]
        if inst == 'nop':
            pos += 1
            continue
        elif inst == 'acc':
            acc += val
            pos += 1
        elif inst == 'jmp':
            pos += val

def one(input):
    """
    >>> one(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'])
    5
    """
    instructions = [(x.split(' ')[0], int(x.split(' ')[1])) for x in input]
    acc, _ = computer(instructions)
    return acc

def two(input):
    """
    >>> two(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'])
    8
    """
    instructions = [(x.split(' ')[0], int(x.split(' ')[1])) for x in input]
    
    for ix, (inst, val) in enumerate(instructions):
        altered_instructions = instructions[:]
        if inst == 'nop':
            altered_instructions[ix] = ('jmp', val)
        elif inst == 'jmp':
            altered_instructions[ix] = ('nop', val)
        else:
            continue
        acc, loop = computer(altered_instructions)
        if not loop:
            return acc

def main():
    input = get_input(day=8)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()