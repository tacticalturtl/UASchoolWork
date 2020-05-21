# Created by: Tyson R. Gant
# Class: INFV 320
# Date: 5/12/2020
# Assignment: Module 7 Capstone


sourcefile = 'wireShark.txt'
outputfile = 'results.txt'
lineformat = "No.     Time           Source                Destination           Protocol Length Info"

with open(sourcefile, 'r') as f:
    source = 0
    dest = 0
    for i, line in enumerate(f):
        if lineformat in line:
            print (line)
            bacon = next(f)
            #print (bacon)
            row = bacon.split()
            source = str(row[2])
            dest = str(row[3])
            #print (source)
            #print (" ")
            #print (dest)