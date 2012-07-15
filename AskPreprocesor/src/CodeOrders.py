#-*- coding: utf-8 -*-
from FileParser import *

class CodeOrders(FileParser):

    def __init__(self,fileName):
        FileParser.__init__(self,fileName);

    def __del__(self):
        FileParser.__del__(self);

    def denary2Binary(self,n,i):
        bStr = ''
        if n < 0: raise ValueError, "must be a positive integer"
        if n == 0: return '0'
        while n > 0 or i>0:
            bStr = str(n % 2) + bStr
            n = n >> 1
            i-=1;
        return bStr

    def execute(self):

        line = self.readLine();
        cells = line.split(" ");
        group = int(cells[1]);
        order = 0;
        #print "group:",group;
        while True:
            line = self.readLine();
            cells = line.split(" ");
            if(line==""): break;
            print "%s\t%s" % (cells[1],self.denary2Binary(((order << 7) | group),10));
            order += 1;


codeOrders=CodeOrders("../orders.txt");
codeOrders.execute();
del codeOrders;