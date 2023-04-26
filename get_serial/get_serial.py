# pip install pyserial
from serial.tools import list_ports
import threading
import os

class serial():

    def __init__(self):
        self.ports=list_ports.comports()
        self.run()
        

    def get_serial_ports(self):
        while True:
            ports = list_ports.comports()
            for port in self.ports:
                if(port not in ports):
                    self.ports.remove(port)
                    self.show_ports()
                    print("Device removed : " + str(port))

            for port in ports:
                if(port not in self.ports):
                    self.ports.append(port)
                    self.show_ports()
                    print("New device : " + str(port))

    def run(self):
        t1=threading.Thread(target=self.get_serial_ports)
        t1.start()
        self.show_ports()

    def show_ports(self):
        os.system("cls")
        print("Total " + str(len(self.ports))+" devices")
        l=[]
        for port in self.ports:
            string=port.device
            string=string.replace("COM","")
            l.append(int(string))
        l.sort()
        print("=====================================")
        for i in l:
            for port in self.ports:
                if(port.device == "COM"+str(i)):
                    print("COM"+str(i)+"\t"+port.description)
        print("=====================================")


                
        
if __name__ == '__main__':
    s=serial()