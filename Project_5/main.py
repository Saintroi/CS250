# Written by Andrew Nelson, December 2014
from ExclusiveThemedTriviaGame import *
from InclusiveThemedTriviaGame import *
import sys

def main():
    game = ExclusiveThemedTriviaGame('cards.txt', 30, "Science & Nature")
    print('--- Play game ---\n')
    game.play(int(sys.argv[1]))
    if game.get_score() >= 3:
        bonus = InclusiveThemedTriviaGame('cards.txt', 30, "Science & Nature")
        print('--- Bonus Round ---\n')
        bonus.play(3)
    print('--- Game over ---')

main()    
