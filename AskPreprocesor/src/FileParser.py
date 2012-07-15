#-*- coding: utf-8 -*-

class FileParser():

    def __init__(self,fileName):
        try:
            self.__fileDesc = open(fileName);
        except:
            print "problem z otwarciem pliku"

    def __del__(self):
        if(self.__fileDesc!=None):
            self.__fileDesc.close();
            del self.__fileDesc;

    def readLine(self):
        return self.__fileDesc.readline();

    def hasNext(self, line):
        return line == "";

    def execute(self):
        None;