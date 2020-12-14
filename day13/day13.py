'''
--- Day 13: Shuttle Search ---

Your ferry can make it safely to a nearby port, but it won't get much further. 
When you call to book another ship, you discover that no ships embark from that port to your vacation island. 
You'll need to get from the port to the nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! 
Each bus has an ID number that also indicates how often the bus leaves for the airport.

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. 
At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, 
then various other locations, and finally returns to the sea port to repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. 
The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. 
The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
'''
import math
with open('day13/input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

departure = input[0]
buses = input[1].split(',')

only_running_buses = [bus for bus in buses if not bus == 'x']

def find_next_departure(dep_time,buses):
    dep_time = int(dep_time)
    time_to_next = {(int(bus_time),int(bus_time)-(dep_time % int(bus_time))) for bus_time in buses}
    return min(time_to_next,key= lambda x: x[1])

next_bus = find_next_departure(departure,only_running_buses)
result = next_bus[0] * next_bus[1]
print('Part 1: ' + str(result))

'''
--- Part Two ---
The shuttle company is running a contest: one gold coin for anyone that can find the earliest 
timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that 
subsequent minute. (The first line in your input is no longer relevant.)

For example, suppose you have the same list of bus IDs as above:

7,13,x,x,59,x,31,19
An x in the schedule means there are no constraints on what bus IDs must depart at that time.
'''
from math import gcd

def find_time(buses):
    data = [(int(index),int(bus)) for (index,bus) in enumerate(buses) if not bus == 'x']

    time = 0
    currentstep = 1
    tested = set()

    found = False
    while not found:
        time += currentstep
        found = True
        for index,bus in data:
            if (time+index) % bus != 0:
                found = False
                break
            else:
                if bus not in tested:
                    tested.add(bus)
                    currentstep = int(bus * currentstep / gcd(bus,currentstep))
    return time

print('Part 2: ' + str(find_time(buses)))