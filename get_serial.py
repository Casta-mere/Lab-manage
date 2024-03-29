# pip install pyserial
from serial.tools import list_ports
import time
import threading
import os

class serial():

    def __init__(self):
        self.parts=list_ports.comports()
        self.run()
        

    def get_serial_ports(self):
        while True:
            ports = list_ports.comports()
            for port in self.parts:
                if(port not in ports):
                    self.parts.remove(port)
                    self.show_ports()
                    print("Device removed : " + str(port))

            for port in ports:
                if(port not in self.parts):
                    self.parts.append(port)
                    self.show_ports()
                    print("New device : " + str(port))

    def run(self):
        t1=threading.Thread(target=self.get_serial_ports)
        t1.start()
        t2=threading.Thread(target=self.read_instruction)
        t2.start()
        self.show_ports()

    def show_ports(self):
        os.system("cls")
        print("Total " + str(len(self.parts))+" devices")
        print("=====================================")
        for port in self.parts:
            print(port)
        print("=====================================")

    def read_instruction(self):
        while True:
            instruction = input()
            match(instruction):
                case "cls":
                    self.show_ports()
                case "":
                    self.show_ports()
                    pass
                case _:
                    pass
                
        
if __name__ == '__main__':
    s=serial()