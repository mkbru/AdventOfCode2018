#!/usr/bin/python
import os

frequency = 0
end = None
dupes = {}
foundDupe = None

def readFile():
    fileContents = []
    f=open("frequencies.txt","r")

    if f.mode == "r":
            contents = f.read().splitlines()
            for line in contents:
                fileContents.append(line)
    f.close()
    return fileContents

def partOne(fileContents):
    frequency = 0

    for val in fileContents:
        frequency += int(val)

    print("Part One: " + str(frequency))

def partTwo(fileContents):
    global fileIterations

    while foundDupe != True:
            findDuplicateFrequency()

def findDuplicateFrequency():
    global frequency
    global foundDupe

    f=open("frequencies.txt","r")

    if f.mode == "r":
        contents = f.read().splitlines()
        for line in contents:
                frequency += int(line)

                if frequency in dupes:
                    print("Part Two: " + str(frequency))
                    foundDupe = True
                    break
                else:
                    dupes[frequency] = frequency
    f.close()

def main():
    fileContents = readFile()
    partOne(fileContents)
    partTwo(fileContents)

main()


