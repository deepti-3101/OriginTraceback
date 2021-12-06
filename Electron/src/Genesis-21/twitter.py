import os
import requests
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import sys
from os import listdir
from os.path import isfile, join
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
import time
import csv
import io
import pprint as pp

cred = credentials.Certificate("D:\\documents\\GitHub\\OriginTraceback\\Electron\\src\\Genesis-21\\fb.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-genesis-21-default-rtdb.firebaseio.com/'
})

ref = db.reference('/searchTestT/')

ref.update({
    'data': 'success'
})

Path("D:/Genesis-21/Searches").mkdir(parents=True, exist_ok=True)

username = "MsChaos8"
password = "sarathabanu"  # Be careful, don't accidentally expose your password when committing
name = "D:/Genesis-21/Searches"
target = "C:\\tmp\\1.jpg"
main = OrderedDict()
a="https://twitter.com/hashtag/INDvNZ?src=hashtag_click"


class hashQueue:
    print("Inside hashQueue")
    pQueue = {}
    processed = []

    def __init__(self, initial_list):
        self.pQueue = initial_list
        print("__init__")

    def nextHash(self, mode):
        print("nextHash")
        sort_orders = sorted(self.pQueue.items(), key=lambda x: x[1], reverse=True)
        print("sort_orders:",sort_orders)
        ref.update({"pQueue" : sort_orders})
        if len(sort_orders) >= 0:
            current = sort_orders[0][0]
            if mode == 1:
                self.processed.append(current)
                self.assignHash(current)
                return current
            else:
                return current
        else:
            return False
    
    def assignHash(self, hash):
        print("assignHash")
        del self.pQueue[hash]

class agent:
    print("agent class")
    options = Options()
    #options.add_argument("--headless")

    options.page_load_strategy = 'eager'

    posDic = {}

    products = []

    driver = webdriver.Chrome("C:\\Users\\aruna\\AppData\\Local\\Programs\\Python\\chromedriver", options=options)
    

    posts = []

    fetch = 0

    def __init__(self, fetch):
        print("__init__ agent")
        self.fetch = fetch
        self.login()

    def login(self):
        print("Loggin in ")
        time.sleep(1)


        # navigate to the url
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        try:
            
            #enter your email
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(username) 
            #clicks on next
            nxtbt=self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
            nxtbt.click()
            time.sleep(3)
            # enter your password
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password) 
            
            # click on the click button  
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
        except:
            print("Already Logged in")
        self.initScrapper(tag_bucket.nextHash(1), self.fetch)



    def initScrapper(self, tag, timeLimit):
        print("Init Scrapper")

        time.sleep(5.4)
        #postDetails = {}

        #hash_list = []
       
        self.driver.execute_script('location.replace("https://twitter.com/search?q=%23'+ tag +'&src=typed_query&f=top")')
        url='https://twitter.com/search?q=%23'+ tag +"&src=typed_query&f=top"
        time.sleep(5.4)
 

        for i in range(int(timeLimit)):
            time.sleep(6)
            print(i)

            #self.driver.execute_script("window.scrollTo(0,150)")

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            content = self.driver.execute_script("return document.body.innerHTML;")
            
            
            


            

    

 

                

tag_bucket = hashQueue({"Summer": 1})

agent1 = agent(10)

# agent2 = agent(2)


