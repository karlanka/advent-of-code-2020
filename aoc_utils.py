import os

def get_input(day):
    with open(os.path.join('input', 'day_{}.txt'.format(day))) as f:
        return f.read().splitlines()

def get_input_no_line(day):
    with open(os.path.join('input', 'day_{}.txt'.format(day))) as f:
        return f.read()
