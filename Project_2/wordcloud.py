# Written by Andrew Nelson, October 2014
from wordfrequency import WordFrequency
from word import Word
import math

class WordCloud():
    def __init__(self, count, frequency, stop_words):
        self._max = frequency.maximum()
        self._min = frequency.minimum()
        self._words = []
        self._stop = stop_words
        self.__make__(frequency, count)
        self._f = frequency

    def __make__(self, frequency, count):       #Places word objects into the ._word variable
        w = sorted(frequency.words())
        for word in w:
            if word in self._stop:
                w.remove(word)
        d = {}
        for word in w:
            if frequency.frequency(word) not in d:
                d[frequency.frequency(word)] = word
        order = []
        for k in d.keys():
            order.append(k)
        order = sorted(order)    
        for n in reversed(order):    
            self._words.append(Word(d[n],n))


    def save(self, filename):                   #Writes the words to a text file
        write = open(filename, 'w')
        for i in self._words:
            write.write(i.get_text() + ':' + str(i.get_size())+"\n")
    

class HtmlWordCloud(WordCloud):
    
    def __init__(self,count, frequency, stop_words):
        super().__init__(count, frequency, stop_words)

    def save(self,filename):                    #Writes the words to an html file
        w = open(filename, 'w')
        w.write("<html>")
        w.write("   <head>")
        w.write("   </head>")
        w.write("   <body>")
        k = 1
        for i in self._words:
            w.write("       <tr>")
            w.write("           <td><span style = \"font-size:"+self.font_size(i)+"pt\">"+i.get_text()+"</span></td>")
            if k == 5:
                w.write("       </tr")
                w.write("       <tr>")
                k = 1
            else:
                k+=1

    def font_size(self, word):                  #Used to find the correct font size for each word based on its frequency
        max_size = math.log(self._max) 
        min_size = math.log(self._min) 

        font = math.log(word.get_size())
        
        lowerBound = min_size
        for i in range(0,91,1):
            upperBound = min_size + ((i+1)/91)*(max_size-min_size)
            if font == min_size:
                return "10"
            if font > lowerBound and font<= upperBound:
                return str(10+i)
            lowerBound = upperBound    
