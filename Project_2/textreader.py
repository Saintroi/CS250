
import string

class TextReader:
    def __init__(self, filename):
        self._f = open(filename, 'r')

    def get_word(self):
        token = None
        chars = []
        # while True:
        c = self._f.read(1)
        while c:
            # if c not in [' ', '\n', '\t']:
            if c not in string.whitespace:
                chars.append(c)
            else:
                token = ''.join(chars).strip('"!(),;.')
                if token != '':
                    break  # we have a word, drop out of the loop
                   
                chars = []
            c = self._f.read(1)
        return token

