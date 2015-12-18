#!/usr/bin/python

import sys

def parseLine(line):
    '''
    Parse the line from 'lxwxh' and return as a tuple (l, w, h)
    '''
    # Split the line by each 'x' in the input to a list
    parts = line.split('x')
    # Don't assume your input is good!
    # Check that we actually got the 3 dimensions we were expecting
    if len(parts) != 3:
        raise Exception("expected exactly 3 dimensions, got %d" % len(parts))

    # Return the length, width, and height as a tuple
    # We need to convert the strings in the split string into integers using `int`
    # The map function is a useful way of running a single function on every element in a list
    # So the following is the same as doing this:
    #     lst = []
    #     for part in parts:
    #         lst.append(int(part))
    #     return tuple(lst)
    # The tuple function converts a list into a tuple
    return tuple(map(int, parts))

def calculateNeededWrappingPaperAndRibbon(l, w, h):
    '''
    Calculate the amount of wrapping paper and ribbon needed for a box with
    dimensions with length l, width w, and height h
    '''
    # We need to calculate the total surface area needed for the wrapping
    # the present. To calculate the surface area, the formula is:
    #    (2 * l * w) + (2 * w * h) + (2 * l * h)
    wrappingPaper = (2 * l * w) + (2 * w * h) + (2 * l * h)

    # To calculate the amount of ribbon needed, we need to find the amount
    # needed for both the bow and for wrapping the present. To wrap the
    # present, we need the two dimensions with lowest values (so for 2x3x4, we
    # need 2 and 3).  Since we don't know which attribute has the smallest
    # dimension, we put all of them into an array, sort it, and then take the
    # lowest 2. We then calculate the amount of ribbon by doubling each of
    # these two numbers because there are 4 sides to the present.
    x, y = sorted([l, w, h])[:2]
    ribbon = (2 * x) + (2 * y)

    # We also need to add extra slack for the wrapping paper equal to the area
    # of the smallest side. Since we got the two lowest, we can use those to
    # get the area of the smallest side!
    wrappingPaper += x * y

    # The perfect bow is equal to the cubic feet of volume of the present, so
    # add that to the amount of ribbon needed.
    ribbon += l * w * h
    return wrappingPaper, ribbon

def main():
    amountOfWrappingPaper, amountOfRibbon = 0, 0
    for line in sys.stdin:
        # Parse the line from standard input
        l, w, h = parseLine(line)

        # Calculate the needed wrapping paper and ribbon for this line
        wrappingPaper, ribbon = calculateNeededWrappingPaperAndRibbon(l, w, h)

        # Add the returned values to our sums
        amountOfWrappingPaper += wrappingPaper
        amountOfRibbon += ribbon

    print 'Amount of Wrapping Paper Needed:', amountOfWrappingPaper
    print 'Amount of Ribbon Needed:', amountOfRibbon

if __name__ == '__main__':
    main()
