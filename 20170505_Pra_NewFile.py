#!/usr/bin/python3

#Open an old file and read
R = open("test.txt", "r")  
print(R.readline())


#Open an old file and write
W = open("test.txt", "a")
W.write('I Add A Line')
