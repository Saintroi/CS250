# Written by Andrew Nelson, October 2014

class TextReader():
    
    def __init__(self,filename):
        self._file = open(filename)
    
    def get_word(self):
        word = ''
        pun = ['!','"','(',')',',','.',';']
        white = [' ','  ','\n']
        newchar = self._file.read(1)
        if newchar == '':
            eof = True
        while newchar not in white: 
            word+= newchar
            newchar = self._file.read(1)
            if newchar == '':
                return newchar 

        if len(word) < 1: 
            return self.get_word()
        
        for i in pun:
            word = word.strip(i)
        
        return word.lower()    
