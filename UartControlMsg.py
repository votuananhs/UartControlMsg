#########################################################################################
#
#
#########################################################################################

import os
import sys
import json
import serial


class UartControlMsg():
    configFile = None
    dataConfig = None
    startChar = None
    endChar = None


    def __init__(self,
                 port=None,
                 baudrate=115200,
                 bytesize=serial.EIGHTBITS,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 configFile="./ConfigUart/default.json"):
        self.serial = serial.Serial(port, baudrate, bytesize, parity, stopbits)
        self.configFile = configFile

    def set_config_file(self, _file):
        self.configFile = _file

    def getBaudrateUart(self, input):
        return self.serial.baudrate

    def getByteSize(self, input):
        if (8 == input):
            self.serial.bytesize = serial.EIGHTBITS
        elif (7 == input):
            self.serial.bytesize = serial.SEVENBITS
        elif (6 == input):
            self.serial.bytesize = serial.SIXBITS
        elif (5 == input):
            self.serial.bytesize = serial.FIVEBITS
        else:
            print("wrong value of serial.bytesize")

    def getParity(self, input):
        if (0 == input):
            self.serial.parity = dataConfig["UartControlMsg"]["ConfigUart"]["parity"]
        elif (1 == input):
            self.serial.parity = dataConfig["UartControlMsg"]["ConfigUart"]["parity"]
        else:
            print("wrong value of serial.parity")

    def load_data_config(self):
        tempFile = open(self.configFile, 'r', 'ascii')
        dataConfig  = json.load(tempFile)
        self.serial.port        = dataConfig["UartControlMsg"]["ConfigUart"]["port"]
        self.serial.baudrate    = dataConfig["UartControlMsg"]["ConfigUart"]["baudrate"]
        #self.serial.bytesize    = dataConfig["UartControlMsg"]["ConfigUart"]["bytesize"]
        self.getByteSize(dataConfig["UartControlMsg"]["ConfigUart"]["bytesize"])
        self.serial.parity = dataConfig["UartControlMsg"]["ConfigUart"]["parity"]
        self.serial.stopbits    = dataConfig["UartControlMsg"]["ConfigUart"]["stopbits"]
        self.startChar   = dataConfig["UartControlMsg"]["MessageFrame"]["start_char"]
        self.endChar     = dataConfig["UartControlMsg"]["MessageFrame"]["end_char"]
        # close

    def self_test_data_config(self):
        self.serial.port        = "/dev/tty.SLAB_USBtoUART4"
        self.serial.baudrate    = 115200
        self.serial.bytesize    = serial.EIGHTBITS
        self.serial.parity      = serial.PARITY_NONE
        self.serial.stopbits    = serial.STOPBITS_ONE
        self.startChar   = "~"
        self.endChar     = "~"

    def transmit_data(self, dataMsg):
        print("transmit_data\r\n")
        # start character
        self.serial.write(self.startChar.encode('ascii'))
        # data meesage
        self.serial.write(dataMsg.encode('ascii'))
        # end character
        self.serial.write(self.endChar.encode('ascii'))


    def receive_data(self):
        print("receive_data\r\n")
        #while self.serial.inWaiting() < 0:
        while True:
            if (self.serial.inWaiting() > 0):
                if (self.serial.read(1) == self.endChar):
                    break
                else:
                    print("--> ", self.serial.read(1))

    def run(self, dataMsg):
        try:
            self.serial.open()
        except Exception as e1:
            print("Error open serial port: ", str(e1))
            exit()
        if self.serial.isOpen():
            try:
                # transmit data
                self.transmit_data(dataMsg)
                # receive data
                self.receive_data()
                # close uart port
                self.serial.close()
            except Exception as e2:
                print("Error communicating ...: ", str(e2))
        else:
            print("Cannot open serial port ...")


#########################################################################################
#  MAIN Function
#########################################################################################

test = UartControlMsg()

print("Main Function")
test.load_data_config()
print("baudrate = ", test.GetBaudrateUart())
#test.self_test_data_config()
test.run("hello world")



