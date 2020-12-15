'''
--- Day 14: Docking Data ---

As your ferry approaches the sea port, the captain asks for your help again. 
The computer system that runs this port isn't compatible with the docking program on the ferry, 
so the docking parameters aren't being correctly initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses a strange 
bitmask system in its initialization program. 
Although you don't have the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask or write a value to memory. 
Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, 
a line like mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. 
The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.

Execute the initialization program. What is the sum of all values left in memory after it completes?
'''
def readInsts(inpath="day14/input.txt"):
    with open(inpath, "r") as infile:
        return list(map(lambda x: x.split(" = "), infile.read().splitlines()))


def part1(insts):
    vals = {}
    mask = "X" * 36
    for inst in insts:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            curr = list(mask)
            ind = inst[0][4:-1]
            val = str(bin(int(inst[1])))[2:]
            val = "0" * (len(curr) - len(val)) + val
            for i in range(len(curr)):
                if curr[i] == "X":
                    curr[i] = val[i]
            vals[ind] = int("".join(curr), 2)
    return sum(vals.values())


'''
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. 
It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. 
Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. 
In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!
'''
def part2(insts):
    vals = {}
    mask = "0" * 36
    for inst in insts:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            curr = list(mask)
            ind = str(bin(int(inst[0][4:-1])))[2:]
            ind = "0" * (len(curr) - len(ind)) + ind
            val = int(inst[1])
            floating = []

            for i in range(len(curr)):
                if curr[i] == "0":
                    curr[i] = ind[i]
                if curr[i] == "X":
                    floating.append(i)

            for i in range(2 ** len(floating)):
                currind = curr[:]
                binstr = str(bin(i))[2:]
                binstr = "0" * (len(floating) - len(binstr)) + binstr
                for i, j in zip(floating, binstr):
                    currind[i] = j
                vals["".join(currind)] = val
    return sum(vals.values())


def main():
    insts = readInsts()
    print(f"Part 1: {part1(insts)}\nPart 2: {part2(insts)}")


main()
