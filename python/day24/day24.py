'''
--- Day 24: Lobby Layout ---

Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). 
Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. 
(Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. 
These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, 
esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. 
Tiles might be flipped more than once. 
For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.
'''
import re

with open('day24/input.txt') as file:
    instructions = [line.strip() for line in file.readlines()]

def parse(instruction):
    steps = re.findall(r"e|se|sw|w|nw|ne", instruction)
    y = steps.count("se") + steps.count("sw") - steps.count("ne") - steps.count("nw")
    x = steps.count("e") + steps.count("ne") - steps.count("w") - steps.count("sw")
    return (y,x)

def part_1(instructions):
    black_tiles = dict()
    for instruction in instructions:
        temp = parse(instruction)
        if temp in black_tiles:
            black_tiles[temp] = False
        else:
            black_tiles[temp] = True
    return black_tiles

black_tiles = part_1(instructions)
print('Part 1: ' + str(sum(black_tiles.values())))
'''
--- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?
'''
NEIGHBOURS_OFFSETS = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

def part_2(black_tiles):
    
    current_floor = black_tiles

    day = 0
    while day < 100:
        next_floor = dict()

        # Add neighbours to current floor
        for (y,x) in current_floor:
            for (offset_y,offset_x) in NEIGHBOURS_OFFSETS:
                temp = (y + offset_y, x + offset_x)
                if temp not in next_floor:
                    next_floor[temp] = current_floor.get(temp, False)

        # Flip according to rules
        for (y,x),black_tile in next_floor.items():
            for (offset_y,offset_x) in NEIGHBOURS_OFFSETS:
                neighbours_list = [current_floor.get((y + offset_y, x + offset_x),False) for offset_y,offset_x in NEIGHBOURS_OFFSETS]
            black_tile_neighbours = sum(neighbours_list)

            if black_tile:
                if black_tile_neighbours == 0 or black_tile_neighbours > 2:
                    next_floor[(y,x)] = False
            elif not black_tile:
                if black_tile_neighbours == 2:
                    next_floor[(y,x)] = True
        
        # Update current floor 
        current_floor = next_floor
        day += 1
    return sum([black_tile for tile in current_floor.values()])

print(part_2(black_tiles))
