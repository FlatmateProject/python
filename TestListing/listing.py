import os
import sys

if len(sys.argv) > 1:
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
	    if filename.find("Test.java") != -1:
            	print os.path.join(dirname, filename).replace(sys.argv[1], "").replace("/",".").replace(".java", "")
