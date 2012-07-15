import os
import sys

if len(sys.argv) > 2:
    currentTestsFile = open(sys.argv[1], "r")
    currentTestsList = currentTestsFile.readlines()
    betterTestsFile = open(sys.argv[2], "r")
    betterTestsList = betterTestsFile.readlines()
    for item in betterTestsList:
        local = item[item.rfind(".") + 1:item.find("=")]
	local = "\t" + local + ".class"
	print local
    result = list()
    for testName in result:
        print testName.replace("\n", "") 
