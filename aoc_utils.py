import os

def get_input(day):
    with open(os.path.join('input', 'day_{}.txt'.format(day))) as f:
        return f.read().splitlines()

