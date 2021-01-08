'''
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. 
They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! 
When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); 
the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. 
For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine 
what the configuration of cubes should be at the end of the six-cycle boot process.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?
'''
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product, chain


def neighbours(point):
    n = len(point)

    for delta in product(range(-1, 2), repeat=n):
        if any(val != 0 for val in delta):
            yield tuple([point[i] + delta[i] for i in range(n)])

def part_1(config, repetions):
    active = {(x, y, 0) for y, line in enumerate(config) for x, c in enumerate(line) if c == '#'}

    for _ in range(repetions):
        counts = Counter(chain.from_iterable(neighbours(a) for a in active))
        active = {k for k,v in counts.items() if v == 3 or (k in active and v == 2)}
    
    return len(active)


file = open('day17/input.txt','r')
config = [row.strip() for row in file.read().split()]

print('Part 1 ' + str(part_1(config, 6)))

'''
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, 
its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. 
(In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?
'''
def part_2(config, repetions):
    active = {(x, y, 0, 0) for y, line in enumerate(config) for x, c in enumerate(line) if c == '#'}

    for _ in range(repetions):
        count = Counter(chain.from_iterable(neighbours(a) for a in active))
        active = {k for k,v in count.items() if v == 3 or (k in active and v == 2)}
    
    return len(active)


print('Part 2: ' + str(part_2(config, 6)))