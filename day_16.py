from aoc_utils import get_input, get_input_no_line
import sys
import time
import re
import collections
import math

def make_rule_set(rules):
    rule_set = set()
    for rule in rules:
        v1, v2, v3, v4 = map(int, re.findall(r'\d+', rule))
        rule_set.update(range(v1, v2+1))
        rule_set.update(range(v3, v4+1))
    return rule_set

def validate_ticket(ticket, rule_set):
    error_rate = 0
    valid = True
    for value in map(int, ticket.split(',')):
        if value not in rule_set:
            error_rate += value
            valid = False
    return error_rate, valid

def one(rules, nearby):
    """
    >>> one(['class: 1-3 or 5-7','row: 6-11 or 33-44','seat: 13-40 or 45-50'], ['7,3,47','40,4,50','55,2,20','38,6,12'])
    71
    """
    rule_set = make_rule_set(rules)
    
    error_rate = 0
    for ticket in nearby:
        error_rate += validate_ticket(ticket, rule_set)[0]

    return error_rate

def make_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        rule_set = set()
        rule_name = rule.split(':')[0]
        v1, v2, v3, v4 = map(int, re.findall(r'\d+', rule))
        rule_set.update(range(v1, v2+1))
        rule_set.update(range(v3, v4+1))
        rule_dict[rule_name] = rule_set
    return rule_dict


def two(rules, nearby, my_ticket):
    rule_set = make_rule_set(rules)
    rule_dict = make_rule_dict(rules)

    ix_dict = collections.defaultdict(set)

    for ticket in nearby:
        if validate_ticket(ticket, rule_set)[1]:
            for ix, val in enumerate(map(int, ticket.split(','))):
                ix_dict[ix].add(int(val))

    my_ticket = list(map(int, my_ticket.split(',')))
    for ix, val in enumerate(my_ticket):
        ix_dict[ix].add(val)

    field_dict = collections.defaultdict(set)
    for ix, values in ix_dict.items():
        for rule, rule_values in rule_dict.items():
            if values.issubset(rule_values):
                field_dict[rule].add(ix)
            
    field_dict = {k: v for k, v in sorted(field_dict.items(), key=lambda item: len(item[1]))}
    
    for k, v in field_dict.items():
        for k_inner, v_inner in field_dict.items():
            if k != k_inner:
                field_dict[k_inner] = v_inner - v
    
    departures = [my_ticket[list(v)[0]] for k, v in field_dict.items() if 'departure' in k]
    return math.prod(departures)

def main():
    input = get_input(day=16)
    ix_my_ticket = input.index('your ticket:')
    my_ticket = input[ix_my_ticket + 1]
    nearby = input[input.index('nearby tickets:') + 1:]
    
    start = time.time()
    print("first:", one(input[:ix_my_ticket - 1], nearby))
    print('It took', time.time() - start, 'seconds for first.')
    
    start = time.time()
    print("second:", two(input[:ix_my_ticket-1], nearby, my_ticket))
    print('It took', time.time() - start, 'seconds for second.')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()