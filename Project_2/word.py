# Written by Andrew Nelson, October 2014

class Word():                      #Represents a word 
    
    def __init__(self,text,size):
        self._text = text
        self._size = size
        
    def get_text(self):
        return self._text

    def get_size(self):
        return self._size

    def set_text(self, text):
        self._text = text

    def set_size(self, size):
        self._size = size

