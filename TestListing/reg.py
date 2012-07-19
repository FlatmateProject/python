import os
import sys

if len(sys.argv) > 2:
    currentTestsFile = open(sys.argv[1], "r")
    currentTestsList = currentTestsFile.readlines()
    result = [item for item in currentTestsList if item.find(sys.argv[2]) == -1]
    for testName in result:
        print testName.replace("\n", "") 
