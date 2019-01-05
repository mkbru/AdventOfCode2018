#!/usr/bin/python
import os

frequency = 0
end = None
dupes = {}
foundDupe = None
fileIterations = 0

def computeFrequencies():
    global frequency
    global foundDupe

    f=open("frequencies.txt","r")
    f2=open("copiedFrequencies.txt","a")

    if f.mode == "r":
        contents = f.read().splitlines()
        
        for line in contents:

            if line[0] == '+':
                frequency += int(line[1:end])
            else:
                frequency -= int(line[1:end])

            print >>f2,frequency

            if frequency in dupes:
                print("***Part Two***")
                print("First frequency the device reaches twice: " + str(frequency))
                foundDupe = True
                break
            else:
                dupes[frequency] = frequency

    f.close()
    f2.close()

def iterateFile():
    global fileIterations

    while foundDupe != True:
        computeFrequencies()
        fileIterations += 1

        if fileIterations == 1:
            print("***Part One***")
            print("Resulting frequency after all the changes have been applied: " + str(frequency))

iterateFile()

def dayOne():
    if os.path.exists("copiedFrequencies.txt"):
        os.remove("copiedFrequencies.txt")
    else:
        print("The file does not exist")
