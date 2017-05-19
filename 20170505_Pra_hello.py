#!/usr/bin/python3
import sys

def main():
    print (sys.argv)
    if len(sys.argv) < 2:
        print ("Usage:", sys.argv[0], "<WHO>")
        sys.exit(1)
        
    who = sys.argv[1] + sys.argv[2]
    
    print ("Hello, {}" .format(who))
    
if __name__ == "__main__":
    main()
