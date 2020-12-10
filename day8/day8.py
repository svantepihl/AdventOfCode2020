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


    while pos not in visited or pos == len(commands):
        visited.add(pos)
        
        # Parse command into operation and argument
        command = commands[pos]
        op, arg = command.split()

        # Perform operation
        if op == 'acc':
            acc += int(arg)
            pos += 1

        elif op == 'jmp':
            pos += int(arg)
            
        elif op == 'nop':
            pos += 1
    # Return final position and accumalator value
    return acc


# Read input
file = open('day8/input.txt','r')
commands = file.read().strip().split('\n')

# Get result:
result = solve_1(commands)
print("Value of accumalator before any repeted commands is: " + str(result))

'''
--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. 
(No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. 
By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). 
What is the value of the accumulator after the program terminates?
'''
def solve_2(commands):
    # Get position of all possible changes to make
    possible_changes = [pos for pos in range(len(commands)) if 'jmp' in commands[pos] or 'nop' in commands[pos]]
    
    # Iterate through and check change by change
    for change_pos in possible_changes:
        
        # Make copy of orginal commands
        new_commands = [command for command in commands]

        # Make change to commands
        if 'jmp' in new_commands[change_pos]:
            new_commands[change_pos] = new_commands[change_pos].replace('jmp', 'nop')
        elif 'nop' in new_commands[change_pos]:
            new_commands[change_pos] = new_commands[change_pos].replace('nop','jmp')
        
        # Keep track of important things
        visited = set()
        pos = 0
        acc = 0
        
        while pos not in visited:

            # If end of commands reached return current accumulator
            if pos == len(new_commands):
                return acc

            # Add current posistion set of visited
            visited.add(pos)
        
            # Parse command into operation and argument
            command = new_commands[pos]
            op, arg = command.split()

            # Perform operation
            if op == 'acc':
                acc += int(arg)
                pos += 1
            elif op == 'jmp':
                pos += int(arg)
            elif op == 'nop':
                pos += 1






print(solve_2(commands))