import sys
import os
from memory import *
from disk import *
from archive import *
from picvideo import *
from utils import *
from network import *
from unknown import *

forOptions = dict(
        Disk = 1,
        Memory = 2,
        Network = 3,
        Archive = 4,
        Picvideo = 5,
        Unknown = 6,
)
print '''
 #     # #       ####### ### #     #    #    ####### #######
 #     # #          #     #  ##   ##   # #      #    #
 #     # #          #     #  # # # #  #   #     #    #
 #     # #          #     #  #  #  # #     #    #    #####
 #     # #          #     #  #     # #######    #    #
 #     # #          #     #  #     # #     #    #    #
  #####  #######    #    ### #     # #     #    #    #######
'''

while True:
    try:
        filename = raw_input("Enter the full path to the file you wish to analyze: ")
        f = open(filename, "rb")
        break
    except IOError:
        print "No such file exists. Check your directory structure and try again...\n"
        continue

print "\nThe following options are available:"
print "1) Disk forensics\n2) Memory forensics\n3) Network forensics\n4) Archive forensics\n5) Picture/video forensics\n6) Unknown forensics\n"

while True:
    try:
        option = raw_input("Enter a number 1-6 to choose a method of forensics: ")
        i_opt = int(option)
        if 0 < i_opt and 7 > i_opt:
            pass
        else:
            print "Invalid number. Try again..."
            continue
        break
    except ValueError:
        print "You failed. Enter a number please..."

if i_opt == 1:
    disk.Disk(filename)
elif i_opt == 2:
    memory.Memory(filename)
elif i_opt == 3:
    network.Network(filename)
elif i_opt == 4:
    archive.Archive(filename)
elif i_opt == 5:
    picvideo.Picvideo(filename)
else:
    unknown.Unknown(filename)
