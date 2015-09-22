
from textreader import TextReader

class WordFrequency:

    def __init__(self):
        self._freqs = {}
        self._max = -1
        self._min = -1

    def open(self, filename):
        reader = TextReader(filename)
        word = reader.get_word()
        while word:
            if word not in self._freqs:
                self._freqs[word] = 1
            else:
                self._freqs[word] += 1
            word = reader.get_word()
        vals = self._freqs.values()
        self._max = max(vals)
        self._min = min(vals)

    def maximum(self):
        return self._max

    def minimum(self):
        # return min(self._freqs.values())
        return self._min

    def words(self):
        return list(self._freqs.keys())

    def frequency(self, word):
        if word in self._freqs.keys():
            return self._freqs[word]
        else:
            return -1

    def save(self,file):
        with open(file,'w') as f:
            for word in sorted(self._freqs.keys()):
                f.write(word + ':' + str(self._freqs[word]) +'\n')
                
