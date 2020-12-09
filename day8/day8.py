'''
--- Day 8: Handheld Halting ---

Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu 
for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. 
You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. 
Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. 
For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. 
After an acc instruction, the instruction immediately below it is executed next.

jmp jumps to a new instruction relative to itself. 
The next instruction to execute is found using the argument as an offset from the jmp instruction; 
for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and 
jmp -20 would cause the instruction 20 lines above to be executed next.

nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
'''
def solve_1(commands):
    # Keep track of accumalator and current position
    acc = 0
    pos = 0

    # Keep track of visited positions
    visited = set()


    while True:
        if pos == len(commands) or pos in visited:
            break
        else:
            visited.add(pos)
        
        # Parse command into operation and argument
        command = commands[pos]
        op, arg = command.split()

        #
        if op == 'acc':
            acc += int(arg)
            pos += 1
        elif op == 'jmp':
            if int(arg) + pos < len(commands):
                pos += int(arg)
            else:
                print('Jump command at ' + pos +' leads to out of bounds.')
        elif op == 'nop':
            pos += 1
    # Return final position and accumalator value
    return pos, acc


# Read input
file = open('day8/input.txt','r')
commands = file.read().strip().split('\n')

# Get result:
result = solve_1(commands)[1]
print("Value of accumalator before any repeted commands is: " + str(result))