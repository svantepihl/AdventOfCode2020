'''
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. 
As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. 
You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). 
For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. 
All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). 
The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
'''
from copy import copy, deepcopy
# Read input
seating_input = list()
with open('day11/input.txt') as file:
    for row in file.readlines():
        seating_input.append(list(row.strip()))

def get_adjacents(matrix,x,y):
    cols = [i for i in range(x-1,x+2) if i in range(len(matrix[0]))]
    rows = [i  for i in range(y-1,y+2) if i in range(len(matrix))]

    return [matrix[row][col] for col in cols for row in rows if not (col,row) == (x,y)]


def process_seating_1(seating):
    
    # Initialize varible to keep track of if seating changed
    changed = False

    # Dimensions of seating
    height = len(seating)
    width = len(seating[0])
    
    while True:
        # Deep copy
        new_seating = [list(line) for line in seating]

        changed = False
        for row in range(height):
            for col in range(width):
                # Skip if position is a 'floor' 
                if seating[row][col] == '.':
                    continue
                
                adjacents = get_adjacents(seating,col,row)
                occupied = adjacents.count('#')
                
                if seating[row][col] == 'L' and occupied == 0:
                    new_seating[row][col] = '#'
                    changed = True

                if seating[row][col] == '#' and occupied >= 4:
                    new_seating[row][col] = 'L'
                    changed = True
        
        if not changed:
            break
        
        seating = new_seating

    return sum(row.count('#') for row in new_seating)


print('Part 1: ' + str(process_seating_1(seating_input)))

'''
--- Part Two ---
As soon as people start to arrive, you realize your mistake. 
People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. 

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). 
The other rules still apply: 
empty seats that see no occupied seats become occupied, 
seats matching no rule don't change, 
and floor never changes.
'''

def get_visable_seats(matrix,x,y):
    # Dimensions of matrix
    height = len(matrix)
    width = len(matrix[0])

    # List of values for all 8 directions
    up = [matrix[y-i][x] for i in range(1,y+1)]
    down = [matrix[y+i][x] for i in range(1,height-y)]
    left = [matrix[y][x-i] for i in range(1,x+1)]
    right = [matrix[y][x+i] for i in range(1,width-x)]
    
    ne = [matrix[y-i][x+i] for i in range(1,min(width-x,y+1))]
    se = [matrix[y+i][x+i] for i in range(1,min(width-x,height-y))]
    sw = [matrix[y+i][x-i] for i in range(1,min(x+1,height-y))]
    nw = [matrix[y-i][x-i] for i in range(1,min(x+1,y+1))]

    return [up,down,left,right,ne,se,sw,nw]
    


def count_occupied_seats_visable(seating,x,y):
    directions = get_visable_seats(seating,x,y)
    return int(sum(map(first_seat_occupied,directions)))


def first_seat_occupied(direction):
    for seat in direction:
        if seat == 'L':
            return False
        if seat == '#':
            return True
    return False

def process_seating_2(seating):
    
    # Initialize varible to keep track of if seating changed
    changed = False

    # Dimensions of seating
    height = len(seating)
    width = len(seating[0])
    
    while True:
        # Deep copy
        new_seating = [list(line) for line in seating]

        changed = False
        for row in range(height):
            for col in range(width):
                current_pos = seating[row][col]
                # Skip if position is a 'floor' 
                if current_pos == '.':
                    continue
                
                # Get number of visable occupied seats
                occupied = int(count_occupied_seats_visable(seating,col,row))
                
                if current_pos == 'L' and occupied == 0:
                    new_seating[row][col] = '#'
                    changed = True

                if current_pos == '#' and occupied >= 5:
                    new_seating[row][col] = 'L'
                    changed = True
        
        if not changed:
            break
        
        seating = new_seating

    return sum(row.count('#') for row in new_seating)
        
    
print('Part 2: ' + str(process_seating_2(seating_input)))