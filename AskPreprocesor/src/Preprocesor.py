#-*- coding: utf-8 -*-
from Definition import *
from sys import stdout
from binascii import *
from FileParser import *

class Preprocesor(FileParser):

    def __init__(self,fileName,definition):
        FileParser.__init__(self,fileName);
        self.__definition = definition;
        self.__stackTrace = list();

    def __del__(self):
        FileParser.__del__(self);

    def execute(self):
        i=1;
        cycleName = "";
########configuration###############################
        order = 3
        group = 38
        resolution = 14;
####################################################
        micro = 0;
        address = ((order << 7) + group) << 4;
        #print "adres:",address, self.__definition.denary2Binary(address,resolution)
        while True:
            line = self.readLine();
            if(line==""): break;
            if (i % 5 == 0):
                line=line[0:line.find("\n")]
                elements=line.split("\t");
                #print elements;
                self.__translate(elements,cycleName,address,resolution,micro,i);
                address+=1;
                micro+=1;
            elif (i % 5 == 2): cycleName=line[0:line.find("\n")]
            i+=1;

    def __translate(self,elements,cycleName,address,resolution,micro,lineNo):
        try:
            self.__definition.printLn(elements,cycleName,address,resolution);
        except Exception, e:
            self.__stackTrace.append("[line %3d] micro %2d invalid key: %s -> %s" % (lineNo,micro,e,cycleName));

    def showStackTrace(self):
        if(len(self.__stackTrace)>0): print "\nError message"
        for errorMsg in self.__stackTrace:
            print errorMsg;

preprocesor = Preprocesor("../microinstruction.txt",Definition());
preprocesor.execute();
preprocesor.showStackTrace();
del preprocesor;
