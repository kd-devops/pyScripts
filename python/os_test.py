#/bin/python
import os
import sys
file1=open("foo.txt", "a+")
file1.write("testing sys.argv.\n")
arg1 = sys.argv[1]
arg2 = sys.argv[2]
args = arg1 + arg2
file1.write(args)
file1.close()

data = open ("foo.txt", "r+")
print data.read()

