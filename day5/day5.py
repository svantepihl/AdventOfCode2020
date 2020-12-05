'''
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with 
the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", 
L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). 
Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) 
or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
'''
import re
boarding_pass_pattern = re.compile('([FB]{7})([RL]{3})')

def generate_ticket_id(boarding_pass):
    if boarding_pass_pattern.match(boarding_pass):
        # Convert to binary
        bp_binary = boarding_pass.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        
        # Parse convert string binary to int
        ticket_id = int(bp_binary,2)
        
        return ticket_id
    else:
        print('Not a valid boarding pass!')

# Read input from file and split into list
file = open('day5/input.txt','r')
boarding_passes = file.read().split()

# Generate ticket ids for all boarding passes
ticket_ids = list(map(generate_ticket_id,boarding_passes))

# Get largest ticket id
max_ticket_id = max(ticket_ids)

print('Largest ticket id: ' + str(max_ticket_id))

'''
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, 
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

def find_missing_ticket(tickets):
    return min((ticket+1 for ticket in tickets if ticket+1 not in tickets and ticket+2 in tickets))

my_ticket = find_missing_ticket(ticket_ids)

print('My ticket id: ' + str(my_ticket))