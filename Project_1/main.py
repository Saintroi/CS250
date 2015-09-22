#Written by Andrew Nelson, October 2014
import sys
import wordfrequency

def main():
    readfile = sys.argv[1]

    obj = wordfrequency.WordFrequency()

    obj.open(readfile)

    print("Maximum:",obj.maximum())
    print("Minimum:",obj.minimum())
    obj.save("freq.dat")
    print("Words and their frequencies saved to freq.dat")

main()
