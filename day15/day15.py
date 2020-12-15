'''
--- Day 15: Rambunctious Recitation ---
You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, 
but a route is available to get around the storm. You take it.

While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a memory game and are ever so excited to explain the rules!

In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input). 
Then, each turn consists of considering the most recently spoken number:

If that was the first time the number has been spoken, the current player says 0.
Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age (if the last number is a repeat).

Given your starting numbers, what will be the 2020th number spoken?
'''
puzzle_input = [13,16,0,12,15,1]

def game(puzzle_input,nth_number):
    memory = dict()
    current_turn = 1
    num_spoken, previous = None,None

    while current_turn <= nth_number:
        if current_turn-1 < len(puzzle_input):
            num_spoken = puzzle_input[current_turn-1]
        elif previous not in memory:
            num_spoken = 0
        else:
            num_spoken = current_turn - 1 - memory[previous]

        # Add previous word and previous turn to memory
        memory[previous] = current_turn - 1 

        previous = num_spoken
        current_turn += 1
    return num_spoken

print('2020th number: ' + str(game(puzzle_input,2020)))

'''
--- Part Two ---
Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

Given 0,3,6, the 30000000th number spoken is 175594.
Given 1,3,2, the 30000000th number spoken is 2578.
Given 2,1,3, the 30000000th number spoken is 3544142.
Given 1,2,3, the 30000000th number spoken is 261214.
Given 2,3,1, the 30000000th number spoken is 6895259.
Given 3,2,1, the 30000000th number spoken is 18.
Given 3,1,2, the 30000000th number spoken is 362.
Given your starting numbers, what will be the 30000000th number spoken?
'''

print('30000000th number: ' + str(game(puzzle_input,30000000)))
