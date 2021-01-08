'''
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. 
All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, 
this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. 
For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. 
(Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). 
Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:
'''
import re

# Read input from file and split based on groups
file = open('day6/input.txt','r')
groups = file.read().split('\n\n')

re_alpha = re.compile('[^a-zA-Z]')


all_answers = list(map(lambda x: re_alpha.sub('',x),groups))

results_pt1 = [list(set(answers)) for answers in all_answers]

count_pt1 = sum(map(len,results_pt1))

print("Total number of questions answered yes to: " + str(count_pt1))

'''
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!
'''

def find_common(answers):
    answers = list(map(set,answers))
    result = list(answers[0].intersection(*answers))
    result.sort()
    return result

group_lists = [group.split() for group in groups]

results_pt2 = list(map(find_common,group_lists))

count_pt2 = sum(map(len,results_pt2))
print("Total number of questions answered yes to: " + str(count_pt2))