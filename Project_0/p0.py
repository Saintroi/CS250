import sys

def print_ppm(height):
    width = int(height/2)
    
    print("P3")
    print(height, width)
    print("255")

    red = "134 0 0"
    white = "255 255 255"
    blue = "13 23 87"
    yellow = "239 255 0"
    count1 = 1
    count2 = 1 
    count3 = 1
    count4 = 1

    for i in range(0, int(height),1):
        c = i
        d = width - i
        y = i
        b = width - i
        while c > 0:
            if i >= (width/2):
                if c == count1:
                    print(white)
                    count1+=2
                else:
                    print(red)
            else:        
                print(red)
            c = c-1
        while d > 0:
            if i <= (width):
                if d == count2:
                    print(white)
                    count2 += 1 
                else:
                    print(yellow)
            else:        
                print(yellow)    
            d = d-1
        while y > 0:
            if i >= (width/2):
                if y == count3:
                    print(white)
                    count3+=2
                else:
                    print(yellow)
            else:
                print(yellow)
            y = y-1
        while b > 0:
            if i <= (width/2):
                if b == count4:
                    print(white)
                    count4+=1
                else:
                    print(blue)
            else:        
                print(blue)
            b = b-1

def main():
    height = int(sys.argv[1])
    if height  <= 1280 and height >= 0:
        print_ppm(height)
    else:
        print("The image must be at most 1280 pixels high!",file=sys.stderr)



main()        
