#-*- coding: utf-8 -*-
from FileParser import *

class NumberIncrease(FileParser):

    def __init__(self,fileName):
        FileParser.__init__(self,fileName);

    def __del__(self):
        FileParser.__del__(self);

    def execute(self,offset):
        while True:
            line = self.readLine();
            if(self.hasNext(line)): break;
            print self.plusN(line.split("\t"), offset);

    def plusN(self, cells, offset):
        resultStr = "";
        for c in cells:
            resultStr += self.increaseCell(c, offset) + "\t"
            #print c;
        return resultStr;
    def hasDots(self, str):
        str.find("..") >= 0;


    def increaseCell(self, cell, offset):
        resultCell = "";
        index = cell.find("..");
        if (index == -1):
            resultCell = self.increaseNumberAndConvertToString(int(cell), offset);
        else:
            elements = self.increaseCellWithDots(index,cell, offset);
            resultCell = elements[0] + ".." + elements[1];
        return resultCell;

    def increaseNumberAndConvertToString(self, number, offset):
        return str(number + offset);

    def increaseCellWithDots(self, index, cell, offset):
        number1 = cell[0:index];
        number2 = cell[index+2:];
        return [self.increaseNumberAndConvertToString(int(number1), offset),self.increaseNumberAndConvertToString(int(number2), offset)];


inc = NumberIncrease("../text");
inc.execute(1);
del inc;