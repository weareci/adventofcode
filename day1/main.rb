#!/usr/bin/ruby

# We start on floor zero, not 1
floor = 0
# Keep track of when (and if) we enter the basement
basement = nil

# Keep track of what position we are at
i = 0
STDIN.each_char do |ch|
  # ch is a standard variable name used for 'character'
  # char is another abbreviation, so this iterates over each character

  # We ignore any characters that aren't parenthesis
  # This line executes only if the condition is FALSE
  next unless ['(', ')'].include?(ch)

  case ch
  when '('
    # Go up one floor if we see an open parenthesis
    floor += 1
  when ')'
    # Go down one floor if we see an open parenthesis
    floor -= 1
  end

  # Since we read one character, move the index
  i += 1

  # Check if we have entered the basement for the first time.
  # Since we only care about the first time the basement is entered,
  # we only check if basement is None
  if basement.nil? && floor < 0
    basement = i
  end
end

# Print the answers
puts "Final Floor: #{floor}"
puts "First Move Entering Basement: #{basement}" unless basement.nil?
