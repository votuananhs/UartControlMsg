#########################################################################################
#
#
#########################################################################################

import os
import sys
import json
import serial




class UartControlMsg:
    port = "/"
    baudrate = 115200
    bytesize = 8
    parity = 0
    stopbits = 1
    
    def __init__(self, port, baudrate, bytesize, parity, stopbits):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        
    def SetPortUart(self, port):
        self.port = port
    
    def GetPortUart(self):
        return self.port

    def SetBaudrateUart(self, baudrate):
        self.baudrate = baudrate

    def GetBaudrateUart(self):
        return self.baudrate
    
    def SetByteSizeUart(self, bytesize):
        self.bytesize = bytesize
    
    def GetByteSizeUart(self):
        return self.bytesize
        
    def SetParityUart(self, parity):
        self.parity = parity
        
    def GetParityUart(self):
        return self.parity
        
    def SetStopBitsUart(self, stopbits):
        self.stopbits = stopbits
        
    def GetStopBitsUart(self):
        return self.stopbits
        



#########################################################################################
#  MAIN Function
#########################################################################################


print("Main Function")