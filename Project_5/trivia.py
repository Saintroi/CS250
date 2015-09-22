import csv


class TriviaCard:

    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    def get_question(self):
        return self._question

    def is_answer(self, answer):
        return self._answer == answer


class TriviaGame:

    def __init__(self, filename):
        self._filename = filename
        self._cards = []

    def _make_card(self, data):
        return TriviaCard(data[0], data[1])

    def _read_cards(self):
        with open(self._filename, 'rt') as f:
            for row in csv.reader(f):
                card = self._make_card(row)
                self._cards.append(card)

    def _draw_card(self):
        card = self._cards[0]
        self._cards.pop(0)
        self._cards.append(card)
        return card

    def _play_round(self):
        card = self._draw_card()
        question = card.get_question()
        response = input(question + ' ')
        while not card.is_answer(response):
            print(response, 'is not the correct answer!\n')
            response = input(question + ' ')
        print(response, 'is the correct answer!\n')

    def play(self, num_rounds):
        self._read_cards()
        for i in range(num_rounds):
            print('--- Round', str(i + 1), 'of', num_rounds,'---\n')
            self._play_round()


def main(args):
    if len(args) < 2:
        return 'Usage: {0} number-of-rounds'.format(args[0])
    game = TriviaGame('cards.txt')
    print('--- Play game ---\n')
    game.play(int(args[1]))
    print('--- Game over ---')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
