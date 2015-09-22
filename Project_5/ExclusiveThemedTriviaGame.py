# Written by Andrew Nelson, December 2014
from TimedTriviaGame import *

class ExclusiveThemedTriviaGame(TimedTriviaGame):
    def __init__(self, filename, sec, theme):
        self._time = sec
        self._start = time.time()
        self._filename = filename
        self._cards=[]
        self._score = 0
        self._eTheme = theme
        
    def _draw_card(self):
        card = self._cards[0]
        self._cards.pop(0)
        self._cards.append(card)
        if card.get_theme() == self._eTheme:
            return self._draw_card()
        else:
            return card
    
def main(args):
    game = ExclusiveThemedTriviaGame('cards.txt', 30,"Science & Nature" )
    print('--- Play game ---\n')
    game.play(int(args[1]))
    print('--- Game over ---')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
        

