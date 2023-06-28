import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
import json
import os

def screenShot(filename):
    image = ImageGrab.grab()
    os.mkdir(f"{filename}")
    image.save(f'{filename}/{filename}.png')

def readJson():
    j = json.load(open("macaddr.json", "r", encoding="utf-8"))
    return j

class driver:

    def __init__(self):
        options = webdriver.EdgeOptions()
        self.wd = webdriver.Edge(options=options)
        self.wait = WebDriverWait(self.wd,10,0.5)
        self.devices = readJson()
        self.run()
    
    def run(self):
        self.login()
        for i in self.devices:
            self.get(i, self.devices[i])
        self.wd.quit()

    def login(self):
        self.wd.get("http://121.36.23.86:5601/login")
        self.wd.maximize_window()

        xpath_id = '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/form/div[1]/div[2]/div/div/input'
        id = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_id)))
        id.send_keys("closeli_es")

        xpath_pwd = '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/form/div[2]/div[2]/div/div/input'
        pwd = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_pwd)))
        pwd.send_keys("closeli01\n")

        time.sleep(5)

    def createUrl(self, macaddr):
        time = "2023-06-27T16:00:00.000Z"
        return "http://121.36.23.86:5601/app/discover#/view/d3818090-874b-11ed-a09b-dbd378bf0431?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'" + time +"',to:now))&_a=(columns:!(datasize,livetime,remarks),filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:e6a52330-6ca1-11ed-8d3e-2d4b183ad8c0,key:datasize,negate:!f,params:(query:'0'),type:phrase),query:(match_phrase:(datasize:'0')))),hideChart:!t,index:e6a52330-6ca1-11ed-8d3e-2d4b183ad8c0,interval:auto,query:(language:kuery,query:" + macaddr +"),sort:!(!(time,desc)))"

    def get(self, devicename, devicemac):
        url = self.createUrl(devicemac)
        self.wd.get(url)
        time.sleep(5)
        xpath = '//*[@id="kibana-body"]/div/div/div/div[2]/div/div/div/discover-app/discover/div/main/div/div[3]/div/div/div[1]/div/div[1]/div/div[1]/div/strong'
        try:
            element = self.wait.until(EC.presence_of_element_located(
                (By.XPATH,xpath)))
            offline_count = eval(element.text)
            if(offline_count>1):
                screenShot(f"{devicename}-离线{offline_count}次")
        except:
            print(f"device {devicename} is offline")
d = driver()