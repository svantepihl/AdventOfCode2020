'''
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. 
They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). 
Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. 
Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, 
and are evaluated left-to-right regardless of the order in which they appear.

Before you can help with the homework, you need to understand it yourself. 
Evaluate the expression on each line of the homework; what is the sum of the resulting values?
'''
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product


def part_1(homework):
    t = 0
    for line in homework:
        stack = []
        nums = ''
        val = None
        add = True

        for c in line:
            if c.isdigit():
                nums += c
            elif nums:
                if val:
                    if add:
                        val += int(nums)
                    else:
                        val *= int(nums)
                else:
                    val = int(nums)
                nums = ''
            if c == '+':
                add = True
            elif c == '*':
                add = False
            if c == '(':
                stack.append((val, add))
                val = None
            if c == ')':
                prev = stack.pop()

                if prev[1]:
                    val += prev[0] if prev[0] else 0
                else:
                    val *= prev[0] if prev[0] else 1

        if nums:
            if add:
                val += int(nums)
            else:
                val *= int(nums)
        
        t += val

    return t




file = open('day18/input.txt','r')
homework = [row.strip().replace(' ','') for row in file.read().split('\n')]

print('Part 1: '+ str(part_1(homework)))

'''
--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. 
Instead, addition is evaluated before multiplication.
'''
from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product


def solve_straight(l):
    while '+' in l:
        pluspos = -1

        for i, c in enumerate(l):
            if c == '+':
                pluspos = i
                break

        l = l[:pluspos-1] + [l[pluspos-1] + l[pluspos+1]] + l[pluspos+2:]

    return reduce(lambda a,b: a*b, [v for v in l if isinstance(v, int)])


def calc_line(line):
        line_list = list(line)

        for x in range(len(line_list)):
            if line_list[x].isdigit():
                line_list[x] = int(line_list[x])

        while True:
            parens = []
            stack = []

            for i, c in enumerate(line_list):
                if c == '(':
                    stack.append(i)
                elif c == ')':
                    parens.append((stack.pop(), i))

            open = -1
            close = -1

            for o, c in parens:
                if not any(p[0] > o and p[1] < c for p in parens):
                    open = o
                    close = c
                    break

            if open == -1:
                break
            
            line_list = line_list[:open] + [solve_straight(line_list[open+1:close])] + line_list[close+1:]

        return solve_straight(line_list)
    

def part_2(homework):
    return sum(map(calc_line, homework))

print('Part 2: '+ str(part_2(homework)))