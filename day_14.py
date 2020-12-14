from aoc_utils import get_input, get_input_no_line
import sys
import itertools
import re


def mask_value(mask_input, value):
    for ix, bit in mask_input:
        mask = 1 << ix
        value &= ~mask
        if bit:
            value |= mask

    return value


def one(input):
    """
    >>> one(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0'])
    165
    """
    memory = {}
    for row in input:
        instruction, value = row.split(' = ')
        if instruction == 'mask':
            mask = [(i, int(x)) for i, x in enumerate(list(value[::-1])) if x.isdigit()]
        else:
            memory[instruction] = mask_value(mask, int(value))

    return sum(memory.values())


def float_address(mask_input, value):
    first_mask = [
            (i, 1) if x.isdigit() else (i, 0) 
            for i, x in enumerate(list(mask_input[::-1])) if x != '0'
        ]
    
    for ix, bit in first_mask:
        mask = 1 << ix
        value &= ~mask
        if bit:
            value |= mask
    
    ixs = [i for i, x in enumerate(list(mask_input[::-1])) if x == 'X']
    
    values = []
    for combos in itertools.product([0, 1], repeat=len(ixs)):
        values.append(value + sum((bit * pow(2, ix)) for ix, bit in zip(ixs, combos)))

    return values


def two(input):
    """
    >>> two(['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1'])
    208
    """
    memory = {}
    for row in input:
        instruction, value = row.split(' = ')
        if instruction == 'mask':
            mask = value
        else:
            address = re.findall(r'\d+', instruction)[0]
            for adr in float_address(mask, int(address)):
                memory[adr] = int(value)

    return sum(memory.values())


def main():
    input = get_input(day=14)
    print("first:", one(input))
    print("second:", two(input))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()