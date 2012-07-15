import os
import sys

if len(sys.argv) > 2:
    currentTestsFile = open(sys.argv[1], "r")
    currentTestsList = currentTestsFile.readlines()
    betterTestsFile = open(sys.argv[2], "r")
    betterTestsList = betterTestsFile.readlines()
    result = [item for item in betterTestsList if item not in currentTestsList]
    for testName in result:
        print testName.replace("\n", "") 
