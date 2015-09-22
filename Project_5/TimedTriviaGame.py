# Written by Andrew Nelson, December 2014

from solution1 import *
import time

class TimedTriviaGame(ThemedTriviaGame):
    def __init__(self, filename,  sec):
        self._time = sec
        self._start = time.time()
        self._filename = filename
        self._cards = []
        self._score = 0

    def _set_score(self,score):
        self._score = score
    
    def get_score(self):
        return self._score

    def play(self, num_rounds):
        self._read_cards()
        for i in range(num_rounds):
            print('---Round', str(i+1), 'of', num_rounds, '---\n')
            self._play_round()
            self._set_score(self.get_score() +1 )
            if time.time() - self._start >= self._time:
                print("Time up")
                break

def main(args):
    game = TimedTriviaGame('cards.txt', 30)
    print('--- Play game ---\n')
    game.play(int(args[1]))
    print('--- Game over ---')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

