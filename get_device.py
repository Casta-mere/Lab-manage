

devices = ["400IU","6002L","000VL","2005M","800I8","900CE","X000YC","8009F","X2000J","500UG","600YB","X400H1","X800I7","8004I","000P8","400NJ","600U2","600IN","X700L8","5003A","X400UL","300JG","X600TV"]



class mydevice():

    def __init__(self, device_name):
        self.state,self.device_name   = self.init(device_name)
        pass

    def  init(self,device_name):
        if device_name[0]=="X":
            return True,device_name[1:]
        else:
            return False,device_name

    def get_divice_name(self):
        return self.device_name


if __name__ == '__main__':
    my_devices = []
    for device in devices:
        my_devices.append(mydevice(device))
    names=[]
    for i in my_devices:

        names.append(i.get_divice_name())
    for i in names:
        print(i)
    print("=====================================")
    names.sort()
    for i in names:
        print(i)