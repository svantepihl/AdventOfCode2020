'''
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
'''
import itertools,functools, operator
# Helper functions

def strings_to_ranges(strings):
    '''
    Convert list of strings of format 'x..x-y..y' to list of ranges: range(x..x,y..y)
    '''
    result = []
    for string in strings:
        v1,v2 = string.split('-')
        result.append(range(int(v1),int(v2)+1))
    return result

def is_value_in_ranges(value,ranges):
    '''
    Check if value exsists in any range in the list of ranges
    '''
    for range in ranges:
        if int(value) in range:
            return True
    return False


# Read input from file and split based on groups
file = open('day16/input.txt','r')
raw_rules,raw_my,raw_others = file.read().split('\n\n')

rules = {name.strip():strings_to_ranges(values.split(' or ')) for name,values in [rule.split(': ') for rule in raw_rules.split('\n')]}

# Flatten from list of lists to list
valid_ranges = list(itertools.chain.from_iterable([strings_to_ranges(values.split(' or ')) for _,values in [rule.split(': ') for rule in raw_rules.split('\n')]]))

my_ticket = [int(value.strip()) for value in raw_my.replace('your ticket:\n','').replace('\n',',').split(',')]

others_values = [int(value.strip()) for value in raw_others.replace('nearby tickets:\n','').replace('\n',',').split(',')]

other_tickets = [values.split(',') for values in raw_others.replace('nearby tickets:\n','').split('\n')]

def solve_1(tickets,valid_ranges):
    valid_tickets = []
    not_valid = []
    for ticket in tickets:
        valid = True
        for value in ticket:
            if not is_value_in_ranges(int(value),valid_ranges):
                not_valid.append(int(value))
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets,sum(not_valid)

valid_tickets,part_1 = solve_1(other_tickets,valid_ranges)
print('Part 1: ' + str(part_1))

'''
--- Part Two ---

Now that you've identified which tickets contain invalid values, discard those tickets entirely. 
Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. 
The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, 
including your ticket.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. 

What do you get if you multiply those six values together?
'''

def solve_2(my, others, rules):
    # Transpose other tickets so each index becomes a row
    indexes =  list(map(list, zip(*others)))
    
    possible_fields = [set() for _ in range(len(my))]
    correct_order = ['' for _ in range(len(rules))]

    for position in range(len(possible_fields)):
        for field in rules:
            if all([is_value_in_ranges(value,rules[field]) for value in indexes[position]]):
                possible_fields[position].add(field)
    
    while any(not field for field in correct_order):
        pos = next(pos for pos, possible_fields in enumerate(possible_fields) if len(possible_fields) == 1)
        value = possible_fields[pos].pop()
        for potential_vaules in possible_fields:
            if value in potential_vaules:
                potential_vaules.remove(value)
            correct_order[pos] = value

    return functools.reduce(operator.mul, [my[pos] for pos, field in enumerate(correct_order) if field.startswith('departure')], 1)   

print('Part 2: ' + str(solve_2(my_ticket,valid_tickets,rules)))