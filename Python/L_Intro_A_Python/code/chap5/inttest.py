#!c:\python\python.exe
from sys import *

z = long ( maxint )
z1 = -z

print "32-bit machine:"
print "maxint:", z, "-maxint:", -z, "(2 ** 31L) -1:", (2  ** 31L) -1 
print "------------------------------------------------------------------------"
y = (2 ** 63L) - 1
print "64-bit machine:"
print "maxint:", y, "-maxint:", -y
print "------------------------------------------------------------------------"
z = (2 ** 127L) - 1
print "128-bit machine:"
print "maxint:", z, "-maxint:", -z
