'''
--- Day 10: Adapter Array ---

Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. 
Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of jolts. 
Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts 
lower than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. 
(If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!

If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, 
the adapters, and your device. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
'''
# Read input
file = open('day10/input.txt','r')
adapters = file.read().strip().split('\n')
adapters_1 = [int(adapter.strip()) for adapter in adapters]
adapters_2 = [int(adapter.strip()) for adapter in adapters]

def solve_1(jolts):
    # Add start and ending points
    jolts.append(0)
    jolts.append(max(jolts)+3)

    # Sort
    jolts.sort()
    
    # Count one and three differences
    one_jolts = 0
    three_jolts = 0

    # Check differences
    for i in range(1,len(jolts)):
        current_diff = abs(jolts[i] - jolts[i-1])
        
        if current_diff <= 3:
            if current_diff == 1:
                one_jolts += 1
            if current_diff == 3:
                three_jolts += 1
        else:
            print('Difference larger than 3!')

    return one_jolts*three_jolts


print(solve_1(adapters_1))

'''
--- Part Two ---

To completely determine whether you have enough adapters, 
you'll need to figure out how many different ways they can be arranged. 
Every arrangement needs to connect the charging outlet to your device. 
The previous rules about when adapters can successfully connect still apply.

You glance back down at your bag and try to remember why you brought so many adapters; 
there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
'''

def solve_2(jolts):
    jolts.sort()
    result = {0:1}
    for jolt in jolts:
        result[jolt] = 0
        if jolt - 1 in result:
            result[jolt]+=result[jolt-1]
        if jolt - 2 in result:
            result[jolt]+=result[jolt-2]
        if jolt - 3 in result:
            result[jolt]+=result[jolt-3]
    return result[max(jolts)]

print(solve_2(adapters_2))