'''
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. 
The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, 
it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. 
After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. 
(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, 
but would still move east if the following action were F.)

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
'''
import math
class Ship_1:
    def __init__(self):
        self.direction = 0
        self.x_pos = 0
        self.y_pos = 0
    def move(self,movement,amount):
        if movement == 'N':
            self.y_pos += amount
        if movement == 'S':
            self.y_pos -= amount
        if movement == 'E':
            self.x_pos += amount
        if movement == 'W':
            self.x_pos -= amount
        if movement == 'L':
            self.direction = (self.direction + amount) % 360
        if movement == 'R':
            self.direction = (self.direction - amount) % 360
        if movement == 'F':
            self.x_pos += amount * round(math.cos(math.radians(self.direction)))
            self.y_pos += amount * round(math.sin(math.radians(self.direction)))

    def calc_manhattan_distance(self):
        return abs(self.x_pos)+abs(self.y_pos)

'''
--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action 
meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative 
to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. 
The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
'''

class Ship_2:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.waypoint_x_pos = 10
        self.waypoint_y_pos = 1
    def move(self,movement,amount):
        if movement == 'N':
            self.waypoint_y_pos += amount
        if movement == 'S':
            self.waypoint_y_pos -= amount
        if movement == 'E':
            self.waypoint_x_pos += amount
        if movement == 'W':
            self.waypoint_x_pos -= amount
        if movement == 'L':
            radians = math.radians(amount)
            x,y = self.waypoint_x_pos, self.waypoint_y_pos
            self.waypoint_x_pos = round(x * math.cos(radians) - y * math.sin(radians))
            self.waypoint_y_pos = round(y * math.cos(radians) + x * math.sin(radians))
        if movement == 'R':
            radians = math.radians(-amount)
            x,y = self.waypoint_x_pos, self.waypoint_y_pos
            self.waypoint_x_pos = round(x * math.cos(radians) - y * math.sin(radians))
            self.waypoint_y_pos = round(y * math.cos(radians) + x * math.sin(radians))
        if movement == 'F':
            self.x_pos += self.waypoint_x_pos * amount
            self.y_pos += self.waypoint_y_pos * amount

    def calc_manhattan_distance(self):
        return abs(self.x_pos)+abs(self.y_pos)


if __name__ == "__main__":

    file = open('day12/input.txt', 'r') 
    lines = file.readlines()
    commands = [(line[0],int(line[1:].strip())) for line in lines]

    ferry_pt1 = Ship_1()
    ferry_pt2 = Ship_2()

    for command in commands:
        ferry_pt1.move(command[0],command[1])
        ferry_pt2.move(command[0],command[1])
    
    print('Part 1: ' + str(ferry_pt1.calc_manhattan_distance()))
    print('Part 2: ' + str(ferry_pt2.calc_manhattan_distance()))

    