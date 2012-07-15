#-*- coding: utf-8 -*-
from FileParser import *

class DefinitionParser(FileParser):

    def __init__(self,fileName):
        FileParser.__init__(self,fileName);

    def __del__(self):
        FileParser.__del__(self);

    def execute(self):
        index = 0;
        while True:
            line = self.readLine();
            tabIndex = line.find("\t");
            enterIndex = line.find("\x0D");
            if(line==""): break;
            print "\t\t\t\t\t\t\"%s\":\"%s\"," % (line[tabIndex+1:enterIndex],line[0:tabIndex]);


parser=DefinitionParser("../definition.txt");
parser.execute();
del parser;