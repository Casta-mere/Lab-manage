import os
import re
path=r"d:\04_log"


def open(devicename):
    try:
        files=os.listdir(path)
        for f in files:
            if re.match(devicename,f):
                os.startfile(f"{path}\\{f}")
                return True
    except:
        return False

