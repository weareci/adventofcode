#!/usr/bin/ruby

require "set"

Point = Struct.new(:x, :y)

# This class tracks the movements of Santa (or his Robot Helper).
# It keeps track of which houses Santa has visited in a data structure
# called a set. A set is a data structure that will hold exactly one of
# an item. For example, if we have the following set:
#
#     Set.new(['a', 'b'])
#
# If we add 'a' to this set, nothing will change since 'a' is already included.
# If we add 'c' though, we get this:
#
#     Set.new(['a', 'b', 'c'])
#
# Sets are a very efficient way of knowing assigning and comparing membership.
#
# Santa's default position is (0, 0) on a grid and he always visits the house
# at (0, 0) first, so it is always included in the list of visited houses.
class Santa
  # Allow people to read the locations Santa has visited.
  attr_reader :visited

  # This is the constructor. When you create a new Santa object, this code
  # will initialize the object so it can be used.
  #
  # When we use the @ symbol before a variable, these are variables that can
  # only be seen inside of the class. We use the `attr_reader` call above to
  # tell Ruby to add a way of reading one of these variables from inside of the
  # class.
  def initialize
    @x = 0
    @y = 0
    @visited = Set.new([Point.new(0, 0)])
  end

  # Move Santa based on the character passed in. When Santa moves, he will
  # visit the house he is currently at.
  def move(ch)
    # Update the x or y position based on the character
    case ch
    when '<'
      @x -= 1
    when '>'
      @x += 1
    when '^'
      @y += 1
    when 'v'
      @y -= 1
    end

    # Add the current grid position to the set of visited locations We add it
    # as a point since both the x and y coordinates are important. In Ruby,
    # classes made using Struct.new can be used in a Set automatically.
    # There's a good reason why, but the explanation is too long for this
    # comment.
    @visited << Point.new(@x, @y)
  end
end

# Read the path Santa will take this year!
path = STDIN.read.chomp

# Create a new Santa. This object keeps track of where Santa
# currently is and where he has visited.
santa = Santa.new
path.each_char do |ch|
  santa.move(ch)
end

# Print the number of unique locations Santa has visited
puts "Santa Visited #{santa.visited.size} Houses"

# We want to restart our trip with two "Santas"
# One is the real santa, the second is a robot Santa helper.
santa, robot = Santa.new, Santa.new
# Instead of iterating over each character, we go over every
# 2 characters. This way, the inner loop is easier as we don't have
# to think about switching between the different Santas.
# There are other ways to do this, but this is the simplest method.
path.chars.each_slice(2) do |ch1, ch2|
  santa.move(ch1)
  robot.move(ch2)
end

# Use a union operation on the locations Santa and his robot visited
# Sets have a lot of useful operations and a union combines them together.
visited = santa.visited | robot.visited
# Print out the locations visited by both Santa and the Robot Helper
puts "Santa (with Robot Helper) Visited #{visited.size} Houses"
