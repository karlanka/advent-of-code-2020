from aoc_utils import get_input, get_input_no_line
import sys
import re
import networkx as nx
import collections

def one(input):
    """
    >>> one(['light red bags contain 1 bright white bag, 2 muted yellow bags.','dark orange bags contain 3 bright white bags, 4 muted yellow bags.','bright white bags contain 1 shiny gold bag.','muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.','shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.','dark olive bags contain 3 faded blue bags, 4 dotted black bags.','vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.','faded blue bags contain no other bags.','dotted black bags contain no other bags.'])
    4
    """
    G = nx.DiGraph()
    for row in input:
        data = [''.join(x.split(' ')[:2]) for x in re.split(r'[0-9] ', row)]
        parent = data[0]
        if len(data) > 1:
            for child in data[1:]:
                G.add_edge(child, parent)

    return len(nx.predecessor(G, 'shinygold')) - 1

def bagcounter(bag, bags):
    # for each of bags child:
    #   add number of bags n + n * child childs...
    total = 0
    for b, n in bags[bag].items():
        total += n + (n * bagcounter(b, bags))
    return total

def two(input):
    """
    >>> two(['light red bags contain 1 bright white bag, 2 muted yellow bags.','dark orange bags contain 3 bright white bags, 4 muted yellow bags.','bright white bags contain 1 shiny gold bag.','muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.','shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.','dark olive bags contain 3 faded blue bags, 4 dotted black bags.','vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.','faded blue bags contain no other bags.','dotted black bags contain no other bags.'])
    32
    """
    bags = collections.defaultdict(dict)
    #'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    # {light red: {bright white: 1, muted yellow: 2}}
    # 'dotted black bags contain no other bags.'
    # {dotted black: {}}
    for row in input:
        data = [''.join(x.split(' ')[:2]) for x in re.split(r'[0-9] ', row)]
        numbers = map(int, re.findall(r'\d+', row))
        if len(data) > 1:
            bags[data[0]] = {k:v for k,v in zip(data[1:],numbers)}
    
    tot = bagcounter('shinygold', bags)
    return tot

def main():
    input = get_input(day=7)
    
    print("first:", one(input))
    print("second:", two(input))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()