# Written by Andrew Nelson, November 2014
from scanner import Scanner
import sys
import string

def binary_to_decimal(binary_digits):
    dec_val = int(binary_digits[0])*64
    dec_val += int(binary_digits[1])*32
    dec_val += int(binary_digits[2])*16
    dec_val += int(binary_digits[3])*8
    dec_val += int(binary_digits[4])*4
    dec_val += int(binary_digits[5])*2
    dec_val += int(binary_digits[6])*1
    return dec_val

def decode(filename):
    x = Scanner(filename)
    line = x.readtoken()
    while (line != "%%"):
        line = x.readtoken()            # Skip the Header
    key = int(x.readtoken())    
    n = int(x.readtoken())              # Get the frequency and number of binary digits
    
    b_list = []
    for i in range(0,n,1):
        for j in range(0,key,1):
            line = x.readtoken()
        if int(line) % 2 == 0:           # Determine each binary digit and place it in an array   
            b_list.append(0)
        else:
            b_list.append(1)
    d_list = []    
    for i in range(0,int(n/7),1):
        s_list = []
        for j in range(0,7,1):              #split the digits into groups of seven and get their true number
            s_list.append(b_list[j])
        del b_list[0:7]
        d_list.append(binary_to_decimal(s_list))
    
    word = ''
    for i in range(0,len(d_list),1):
        d_list[i] = string.printable[d_list[i]]         # Use the numbers as an index in string.printable
        word+=d_list[i]                                 # to find the intended letter

    print("The message is: ", word)    
def main():
    decode(sys.argv[1])

if __name__ == '__main__':
    main()
