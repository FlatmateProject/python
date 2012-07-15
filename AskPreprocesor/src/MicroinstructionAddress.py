#-*- coding: utf-8 -*-
from FileParser import *

class MicroinstructionAddress():

    def __init__(self):
        None

    def __del__(self):
        None

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
########configuration###############################
        orders = 4
        group = 38
        resolution = 14;
        micros = 16
####################################################
        for order in range(orders):
            orderCode = ((order << 7) + group) << 4;
            #print "[",self.denary2Binary(orderCode, resolution),"]";
            for micro in range(micros):
                print self.denary2Binary(orderCode | micro, resolution);


microAddress = MicroinstructionAddress();
microAddress.execute();
del microAddress;