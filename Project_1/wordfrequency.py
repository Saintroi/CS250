# Written by Andrew Nelson October 2014
import textreader 

class WordFrequency():
    def __init__(self):
        self._freq = {}
    
    def open(self,filename):
        read = textreader.TextReader(filename)
        word = read.get_word()
        while word != '':
#            print(word)
            if(self.frequency(word) == -1):
                self._freq[word] = 1
            else:
                self._freq[word] = self.frequency(word)+1
            word = read.get_word()

    def frequency(self, word):
        if word in self._freq:
            return self._freq[word.lower()]
        else:
            return -1

    def maximum(self):
        xam = 1
        for word in self._freq:
            if self.frequency(word) > xam:
                xam = self.frequency(word)
        return xam        

    def minimum(self):
        nim = 1 
        for word in self._freq:
            if self.frequency(word)<nim:
                nim = self.frequency(word)
        return nim        

    def words(self):
        lst = []
        for word in sorted(self._freq):
            lst.append(word)
        return lst
         
    def save(self, filename):
        write = open(filename,'w')
        for word in sorted(self._freq):
            write.write(word+":"+str(self.frequency(word))+"\n")

