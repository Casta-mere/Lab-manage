import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab

weburl = "http://121.36.23.86:5601/app/discover#/view/d3818090-874b-11ed-a09b-dbd378bf0431?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2023-06-27T16:00:00.000Z',to:now))&_a=(columns:!(datasize,livetime,remarks),filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:e6a52330-6ca1-11ed-8d3e-2d4b183ad8c0,key:datasize,negate:!f,params:(query:'0'),type:phrase),query:(match_phrase:(datasize:'0')))),hideChart:!t,index:e6a52330-6ca1-11ed-8d3e-2d4b183ad8c0,interval:auto,query:(language:kuery,query:xxxxS_a8f1b20b89ff),sort:!(!(time,desc)))"


def screenShot(filename):
    image = ImageGrab.grab()
    image.save(f'{filename}.png')

class driver:

    def __init__(self):
        options = webdriver.EdgeOptions()
        self.wd = webdriver.Edge(options=options)
        self.wait = WebDriverWait(self.wd, 50, 0.2)
        self.login()
        self.get(weburl)

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

    def get(self,url):
        self.wd.get(url)
        time.sleep(5)
        xpath = '//*[@id="kibana-body"]/div/div/div/div[2]/div/div/div/discover-app/discover/div/main/div/div[3]/div/div/div[1]/div/div[1]/div/div[1]/div/strong'
        element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH,xpath)))
        offline_count = eval(element.text)
        if(offline_count>0):
            screenShot()


d = driver()