'''
--- Day 22: Crab Combat ---

It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: 
a small crab that climbed aboard your raft before you left.

Fortunately, it doesn't take long to teach the crab the rules.

Before the game starts, split the cards so each player has their own deck (your puzzle input). 
Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. 
The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. 
If this causes a player to have all of the cards, they win, and the game ends.

Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. 
With 10 cards, the top card is worth the value on the card multiplied by 10.

Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
'''
from copy import deepcopy
# Parse input
file = open("day22/input.txt")

player_1,player_2 = file.read().split('\n\n')

player_1,cards_1 = player_1.split(':')
player_2,cards_2 = player_2.split(':')

game = dict()

game[player_1] = list(map(int, cards_1.split()))
game[player_2] = list(map(int, cards_2.split()))

decks = []
for player,cards in game.items():
    decks.append(cards)

def play(decks):
    deck_1 = decks[0]
    deck_2 = decks[1]

    while len(deck_1) > 0 and len(deck_2) > 1:
        card_1,card_2 = deck_1.pop(0),deck_2.pop(0)

        if card_1 > card_2:
            # Deck 1 takes both cards, place at bottom, winning card on top
            deck_1.append(card_1)
            deck_1.append(card_2)
        elif card_2 > card_1:
            # Deck 2 takes both cards, place at bottom, winning card on top
            deck_2.append(card_2)
            deck_2.append(card_1)
        else:
            # Place back cards at the back of each deck
            deck_1.append(card_1)
            deck_2.append(card_2)
    
    winner = reversed(deck_1) if len(deck_1) > len(deck_2) else reversed(deck_2)
    
    score = 0
    for index,value in enumerate(winner):
        score += (index + 1) * value
    return score


            
print("Part 1: " + str(play(deepcopy(decks))))

'''
--- Part Two ---

You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.

Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). 
Then, the game consists of a series of rounds with a few changes:

Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. 
Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
'''


def recursive_combat(deck_1,deck_2):
    previous_decks = []
    
    while len(deck_1) > 0 and len(deck_2) > 1:
        if (deck_1,deck_2) in previous_decks:
            return 'Player 1'
        else:
            previous_decks.append((deepcopy(deck_1),deepcopy(deck_2)))


        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if len(deck_1) >= card_1 and len(deck_2) >= card_2:
            winner = recursive_combat(deepcopy(deck_1)[:card_1],deepcopy(deck_2)[:card_2])

            if winner == 'Player 1':
                deck_1.append(card_1)
                deck_1.append(card_2)
            elif winner == 'Player 2':
                deck_2.append(card_2)
                deck_2.append(card_1)


        else:
            if card_1 > card_2:
                # Deck 1 takes both cards, place at bottom, winning card on top
                deck_1.append(card_1)
                deck_1.append(card_2)
            elif card_2 > card_1:
                # Deck 2 takes both cards, place at bottom, winning card on top
                deck_2.append(card_2)
                deck_2.append(card_1)
            else:
                # Place back cards at the back of each deck
                deck_1.append(card_1)
                deck_2.append(card_2)
    
    return 'Player 1' if len(deck_2) == 0 else 'Player 2'

deck_1,deck_2 = decks[0],decks[1]
winner = recursive_combat(deck_1,deck_2)

if winner == 'Player 1':
    deck_1.reverse()
    winning_deck = deck_1
else:
    deck_2.reverse()
    winning_deck = deck_2

score = 0
for index,value in enumerate(winning_deck):
    score += (index + 1) * value
print('Part 2: ' + str(score))
