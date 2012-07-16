import os
import sys

def isNotIn(local, currentTestsList):
    for item in currentTestsList:
        if item.find(local) != -1:
           return False
    return True

if len(sys.argv) > 2:
    currentTestsFile = open(sys.argv[1], "r")
    currentTestsList = currentTestsFile.readlines()
    betterTestsFile = open(sys.argv[2], "r")
    betterTestsList = betterTestsFile.readlines()
    result = list()
    for item in betterTestsList:
        local = item[item.rfind(".") + 1:item.find("=")]
	if isNotIn(local, currentTestsList):
	    result.append(item);
    for testName in result:
        print testName.replace("\n", "") 
