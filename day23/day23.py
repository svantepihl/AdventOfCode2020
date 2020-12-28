'''
--- Day 23: Crab Cups ---

The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.

The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five cups in the circle; 
going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.

Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.

The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. 
If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. 
If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.

The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.

The crab selects a new current cup: the cup which is immediately clockwise of the current cup.

After the crab is done, what order will the cups be in? 
Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once

Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?
'''
import sys

input = '219748365'

start_cups = [int(char) for char in input]

def crab_cups(moves,cups):

    current_index = 0

    for _ in range(moves): 

        # Current_cup
        current_cup = cups[current_index]

        # Next three cups
        three_cups = [cups.pop((cups.index(current_cup) + 1) % len(cups)) for _ in range(3)]

        # Destination cup
        if current_cup == min(cups):
            destination_value = max(cups)
        else:
            destination_value = current_cup - 1
        
        while destination_value in three_cups:
                if destination_value == min(cups):
                    destination_value = max(cups)
                else:
                    destination_value -= 1
        destination_pos = cups.index(destination_value)

        # Insert cup 1-3
        for cup in reversed(three_cups):
            cups.insert(destination_pos + 1,cup)
        
        # Update index:
        current_index = (cups.index(current_cup) + 1) % len(cups)

    return cups

final_order = crab_cups(100,start_cups.copy())
result = final_order[final_order.index(1)+1:] + final_order[:final_order.index(1)]


part_1 = ''
for cup in result:
    part_1 += str(cup)
print(part_1)

'''
--- Part Two ---

Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), 
you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the 
highest number in your list and proceeding one by one until one million is reached. 
(For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) 
In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; 
the crab is going to do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. 
You can have them if you predict what the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?
'''
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.nodes = {}

    def insert_left(self, val, prevNode=None) -> Node:
        newNode = Node(val)

        if prevNode is None:
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.prev = prevNode
            newNode.next = prevNode.next
            newNode.prev.next = newNode
            newNode.next.prev = newNode

        self.nodes[val] = newNode
        return newNode

    def pop_next(self, left_node=None) -> int:
        pop_node = left_node.next
        pop_value = pop_node.value

        left_node.next = pop_node.next
        pop_node.next.prev = left_node

        del pop_node
        del self.nodes[pop_value]
        return pop_value

    def find(self, value) -> Node:
        return self.nodes[value]

    def get_list(self, marker=1):
        nums = []
        marker_node = self.nodes[marker]
        nums.append(marker_node.val)

        marker_node = marker_node.next
        while marker_node.val != marker:
            nums.append(marker_node.val)
            marker_node = marker_node.next

        return nums


circle = CircularLinkedList()
prev_node = None

for cup in start_cups:
    prev_node = circle.insert_left(cup, prev_node)
   
for cup in range(max(start_cups)+1, 1000001):
    prev_node = circle.insert_left(cup, prev_node)

current_cup = circle.find(start_cups[0])
for i in range(10000000):
    # Print progress
    if (i/10000000)*1000 % 1 == 0:
        sys.stdout.write('Progress: ' + str(round((i/10000000)*100,2)) + '%\r')
        sys.stdout.flush()
    if i == 10000000-1:
        print('Progress: DONE ')

    
    # Next three cups
    three_cups = [circle.pop_next(current_cup) for _ in range(3)]

    # Destination cup
    if current_cup.value == 1:
        cup = 1000000
    else:
        cup = current_cup.value - 1

    while cup in three_cups:
        if cup == 1:
            cup = 1000000
        else:
            cup -= 1

    # Insert cup 1-3
    destination_cup = circle.find(cup)
    for cup in reversed(three_cups):
        circle.insert_left(cup, destination_cup)

    del destination_cup

    # Update current cup
    current_cup = current_cup.next

cup_one = circle.find(1)
total = cup_one.next.value * cup_one.next.next.value
print(total)