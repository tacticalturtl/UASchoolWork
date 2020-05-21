# Created by: Tyson R. Gant
# Class: INFV 320
# Date: 5/12/2020
# Assignment: Module 7 Capstone


def main():

    print("Opening Source file wireShart.txt....")

    # Reaches out to check line fuction to find proper formatted line
    foundlines = CheckLine()

    # Grabs the source ip from the proper row and sector
    sourceIP = SourceIP()

    # Grabs the destination ip from the proper row and sector
    destIP = DestinationIP()

    print("Opening Output file IPAddresses.txt....")

    # Opens the output file to being writing to it
    output = open(OutputFile(), 'w')

    output.write('{0:20}{1:20}\n'.format("Source", "Destination"))

    # Zips the to values into one so we can list them as collumns in a text file
    for source, dest in zip(sourceIP, destIP):

        output.write('{0:20}{1:20}\n'.format(source, dest))

    # Closes the file    
    output.close()

    print("Closing Source file wireShark.txt....")
    print("Closing Output file IPAddress.txt....")
    
# function sets a variable for the source file
def SourceFile():

    MainFile = 'wireShark.txt'
    return MainFile

# function sets a variable for the export file
def OutputFile():

    ExportFile = 'IPAdresses.txt'
    return ExportFile

# function sets a variable for the proper fromatting of the row we are looking for
def LineFormat():

    linecheck = "No.     Time           Source                Destination           Protocol Length Info"
    return linecheck

# function checks and validates the proper row based on format
def CheckLine():

    # opens the source file and formating
    wirefile = SourceFile()
    lineformat = LineFormat()

    with open(wirefile, 'r') as Wire_Dump:
        
        lst = []

        for i, line in enumerate(Wire_Dump):
            
            #finds the comparative row in the file based off our formating
            if lineformat in line:
                lst.append(line)
            else:
                pass
        return lst

# Grabs the source ip from the proper row and sector
def SourceIP():

    # opens the source file and formating
    wirefile = SourceFile()
    lineformat = LineFormat()

    with open(wirefile, 'r') as File_Dump:
        
        source = 0

        lst1 = []

        for i, line in enumerate(File_Dump):

            #finds the comparative row in the file based off our formating
            if lineformat in line:

                # Goes down one row and splits the date, then grabs the 2 sector item which is the source ip
                IPLine = next(File_Dump)
                row = IPLine.split()
                source = str(row[2])

                # i appened the list so when we return the source IP its sends all items and not just one
                lst1.append(source)

            else:
                pass

        return lst1

# Grabs the destination ip from the proper row and sector
def DestinationIP():

    # opens the source file and formating
    wirefile = SourceFile()
    lineformat = LineFormat()

    with open(wirefile, 'r') as File_Dump:
        
        dest = 0

        lst2 = []

        #finds the comparative row in the file based off our formating
        for i, line in enumerate(File_Dump):

            if lineformat in line:

                # Goes down one row and splits the date, then grabs the 3 sector item which is the destination ip
                IPLine = next(File_Dump)
                row = IPLine.split()
                dest = str(row[3])

                # i appened the list so when we return the destination IP its sends all items and not just one
                lst2.append(dest)

            else:
                pass
        return lst2

main()