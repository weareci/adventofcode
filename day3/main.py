#!/usr/bin/python

import sys

class Santa:
    '''
    This class tracks the movements of Santa (or his Robot Helper).
    It keeps track of which houses Santa has visited in a data structure
    called a set. A set is a data structure that will hold exactly one of
    an item. For example, if we have the following set:

        set(['a', 'b'])

    If we add 'a' to this set, nothing will change since 'a' is already included.
    If we add 'c' though, we get this:

        set(['a', 'b', 'c'])

    Sets are a very efficient way of knowing assigning and comparing membership.

    Santa's default position is (0, 0) on a grid and he always visits the house
    at (0, 0) first, so it is always included in the list of visited houses.
    '''

    def __init__(self):
        '''
        This is the constructor. When you create a new Santa object, this code
        will initialize the object so it can be used.

        The `self` parameter is the variable that holds the object. It is the
        same as `this` in JavaScript, but Python requires classes to put `self`
        as the first parameter to all methods in a class.
        '''
        self.x = 0
        self.y = 0
        self.visited = set([(0, 0)])

    def move(self, ch):
        '''
        Move Santa based on the character passed in. When Santa moves, he will
        visit the house he is currently at.
        '''
        # Update the x or y position based on the character
        if ch == '<':
            self.x -= 1
        elif ch == '>':
            self.x += 1
        elif ch == '^':
            self.y += 1
        elif ch == 'v':
            self.y -= 1

        # Add the current grid position to the set of visited locations
        # We add this as a tuple since both the x and y coordinates are
        # important. Python allows us to use tuples for this, but we cannot
        # use lists.
        # There's a good reason why, but the explanation is too long for this
        # comment. Just know that you can use tuples like this in Python.
        self.visited.add((self.x, self.y))

def main():
    # Read the path Santa will take this year!
    path = sys.stdin.read()

    # Create a new Santa. This object keeps track of where Santa
    # currently is and where he has visited.
    santa = Santa()
    for ch in path:
        santa.move(ch)

    # Print the number of unique locations Santa has visited
    print 'Santa Visited %d Houses' % len(santa.visited)

    # We want to restart our trip with two "Santas"
    # One is the real santa, the second is a robot Santa helper.
    santa, robot = Santa(), Santa()
    # Instead of iterating over each character, we go over every
    # 2 characters. This way, the inner loop is easier as we don't have
    # to think about switching between the different Santas.
    # There are other ways to do this, but this is the simplest method.
    for i in xrange(0, len(path), 2):
        santa.move(path[i])
        # We need to check that there isn't an odd number of characters
        # in the path. If there are, we can't index into the path at that
        # location.
        if i+1 < len(path):
            robot.move(path[i+1])

    # Use a union operation on the locations Santa and his robot visited
    # Sets have a lot of useful operations and a union combines them together.
    visited = santa.visited.union(robot.visited)
    # Print out the locations visited by both Santa and the Robot Helper
    print 'Santa (with Robot Helper) Visited %d Houses' % len(visited)

if __name__ == '__main__':
    main()
