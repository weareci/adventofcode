#!/usr/bin/python

import sys

def main():
    # We start on floor zero, not 1.
    floor = 0
    # Keep track of when (and if) we enter the basement
    basement = None

    # read the input from standard input
    inp = sys.stdin.read()

    # i is a standard variable name used for 'index'
    # ch is a standard variable name used for 'character'
    for i, ch in enumerate(inp):
        if ch == '(':
            # Go up one floor if we see an open parenthesis
            floor += 1
        elif ch == ')':
            # Go down one floor if we see a close parenthesis
            floor -= 1
        # We ignore any other characters (no else is needed)

        # Check if we have entered the basement for the first time.
        # Since we only care about the first time the basement is entered,
        # we only check if basement is None
        if basement is None and floor < 0:
            # We want to keep track of the first move when the basement was entered
            # We have the current move in the variable 'i', but 'i' starts at zero
            # instead of 1, so we add 1 to get the real number.
            basement = i + 1

    # Print the answers
    print 'Final Floor:', floor
    if basement is not None:
        print 'First Move Entering Basement:', basement

# Call the main function if this is called through the python interpreter.
# This is a standard method of writing a script in the Python community.
if __name__ == '__main__':
    main()
