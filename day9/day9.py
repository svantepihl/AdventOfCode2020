'''
--- Day 9: Encoding Error ---

With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. 
Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. 
The two numbers will have different values, and there might be more than one such pair.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) 
which is not the sum of two of the 25 numbers before it.  What is the first number that does not have this property?
'''
# Read input
file = open('day9/input.txt','r')
xmas = file.read().strip().split('\n')

def pairs_exists(numbers,target):
    for num in numbers[:-1]:
        # The two numbers can't be the same
        if not num == target/2:
            complement = target - num
            if complement in numbers:
                return True
    return False

def solve_1(data):
    data = [int(row) for row in data]
    for i in range(25,len(data)):
        if not pairs_exists(data[i-25:i],data[i]):
            return data[i]
    return None


print('Part 1: ' + str(solve_1(xmas)))

'''
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: 
you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

To find the encryption weakness, add together the smallest and largest number in this contiguous range; 
in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
'''
def solve_2(data,target):
    data = [int(row) for row in data]
    for start_pos in range(len(data)-2):
        current_pos = start_pos
        current_sum = 0
        while current_sum < target:
            current_sum += data[current_pos]
            if current_sum == target and current_pos - start_pos > 0:
                return min(data[start_pos:current_pos]) + max(data[start_pos:current_pos])
            current_pos += 1
    return None

print('Part 2: ' + str(solve_2(xmas,solve_1(xmas))))