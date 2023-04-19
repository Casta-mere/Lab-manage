from get_serial import get_serial as se
from get_log import get_log as gl

import threading

class Lab():
    def __init__(self):
        self.serial = se.serial()
        self.serial.run()

    def run(self):
        t=threading.Thread(target=self.read_instruction)
        t.start()

    def read_instruction(self):
        while True:
            instruction = input()
            match(instruction):
                case "cls":
                    self.serial.show_ports()
                case "":
                    self.serial.show_ports()
                    pass
                case _:
                    if not gl.open(instruction):
                        print("No such device") 
                    else:
                        self.serial.show_ports()                             
                    pass

if __name__ == "__main__":
    lab = Lab()
    lab.run()