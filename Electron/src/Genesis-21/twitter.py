import os
import requests
from PIL import Image
import imagehash
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from os import listdir
import pyspeedtest
from os.path import isfile, join
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("fb.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-genesis-21-default-rtdb.firebaseio.com/'
})

ref = db.reference('/searchTest1/')

ref.update({"one": "success"})

Path("D:/Genesis-21/Searches").mkdir(parents=True, exist_ok=True)

username = "dem.odummy"
password = ""  # Be careful, don't accidentally expose your password when committing
name = "D:/Genesis-21/Searches"
target = "C:\\tmp\\1.jpg"
main = OrderedDict()


class hashQueue:
    pQueue = {}
    processed = []

    def __init__(self, initial_list):
        self.pQueue = initial_list
        print(self.pQueue)

    def queueStatus(self):
        return self.pQueue

    def addHashList(self, postlist):
        hash_set = []
        for i in postlist:
            hash_set += postlist[i]["hash"]
        self.addHash(hash_set)

    def addHash(self, hash_list):
        for i in hash_list:
            if i in self.pQueue.keys():
                self.pQueue[i] += 1
            elif i not in self.processed:
                self.pQueue[i] = 1

    def nextHash(self, mode):
        sort_orders = sorted(self.pQueue.items(), key=lambda x: x[1], reverse=True)
        ref.update({"pQueue": sort_orders})
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
        del self.pQueue[hash]

    def getProcessedList(self):
        return self.processed

    def getHashQueue(self):
        return self.pQueue

    def getHashPriority(self, tag):
        if tag in self.pQueue:

            return self.pQueue[tag]
        else:
            return False

    def getCurrentHash(self):
        size = len(self.processed)
        if size > 1:
            return self.processed[-1]
        elif size == 1:
            return self.processed[0]
        else:
            return False


class agent:
    options = Options()

    options.page_load_strategy = 'eager'

    posDic = {}

    products = []

    driver = webdriver.Chrome("D:\Python\chromedriver", options=options)

    posts = []

    fetch = 0

    def __init__(self, fetch1):
        print(fetch1)
        self.fetch = fetch1
        self.login()

    def hashProbe(self, threshold, original):
        print("IN HASHPROBE")
        targetListFile = open(name + "/test.txt", "a")
        with Image.open(original) as imgOri:
            hash1 = imagehash.average_hash(imgOri, 8).hash
        path = "C:\\tmp\\Genesis-21\\"
        files = [f for f in listdir(path) if isfile(join(path, f))]
        pList = []
        for x in files:
            if self.sim(threshold, hash1, x):
                url = x.split(".jpg")[0]
                pList.append(url)
                targetListFile.write(url)
        print(pList)
        self.postDataScrapper(pList)
        targetListFile.close()

    def login(self):
        print("Loggin in ")
        time.sleep(1)

        self.driver.maximize_window()

        # navigate to the url
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        try:
            # finds the username box
            usern = self.driver.find_element_by_name("username")
            # sends the entered username
            usern.send_keys(username)
            # finds the password box
            passw = self.driver.find_element_by_name("password")

            # sends the entered password
            passw.send_keys(password)

            time.sleep(2)

            # finds the login button
            log_cl = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
            log_cl.click()  # clicks the login button
            time.sleep(6)
            ntnow = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")
            ntnow.click()
        except:
            print("Already Logged in")

        self.initScrapper(tag_bucket.nextHash(1), self.fetch)

    def initScrapper(self, tag, timeLimit):

        print("Init Scrapper")

        time.sleep(5.4)

        self.driver.execute_script('location.replace("https://www.instagram.com/explore/tags/' + tag + '/")')

        time.sleep(5.4)

        for i in range(int(timeLimit)):

            time.sleep(6)

            print(i)

            self.driver.execute_script("window.scrollTo(0,150)")

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            content = self.driver.execute_script("return document.body.innerHTML;")

            soup = BeautifulSoup(content, features="lxml")

            for link in content.split('" tabindex="0"><div class="eLAPa">'):
                name1 = ""
                try:
                    name1 = link.split('<a href="')[1]
                except:
                    pass
                if "/p/" in name1 and name1 not in self.products:
                    self.products.append(name1)

            for link in soup.find_all('img'):
                name1 = link.get('src')
                try:
                    if "fbcdn.net/v" in name1 and "2885-19" not in name1 and name1 not in self.posts:
                        self.posts.append(name1)
                except:
                    print("Exception Occurred")

        if len(self.posts) == len(self.products):
            for x in range(len(self.posts)):
                self.posDic[self.products[x].split("/p/")[1]] = self.posts[x]

            return self.download(self.posDic)

        else:
            print("Didn't match")
            print(len(self.posts), len(self.products))
            if len(self.posts) <= len(self.products):
                for x in range(len(self.posts)):
                    self.posDic[self.products[x].split("/p/")[1]] = self.posts[x]
            else:
                for x in range(len(self.products)):
                    self.posDic[self.products[x].split("/p/")[1]] = self.posts[x]

        f = open("jsonLog.txt", "w")
        f.write(str(self.posDic))
        f.close()

        return self.download(self.posDic)

    def download(self, pack):
        print("Downloading")
        for x in pack.keys():
            while True:
                filename = "C:\\tmp\\Genesis-21\\" + x[:-1] + ".jpg"
                file_exists = os.path.isfile(filename)

                if not file_exists:
                    with open(filename, 'wb+') as handle:
                        response = requests.get(pack[x], stream=True)
                        if not response.ok:
                            print(response)
                        for block in response.iter_content(1024):
                            if not block:
                                break
                            handle.write(block)
                else:
                    continue
                break
        self.hashProbe(82, target)

    def sim(self, similarity, hash1, img2):
        try:
            with Image.open("C:\\tmp\\Genesis-21\\" + img2) as imgCK:
                hash2 = imagehash.average_hash(imgCK, 8).hash
            threshold = 1 - similarity / 100
            diff_limit = int(threshold * (8 ** 2))
            if np.count_nonzero(hash1 != hash2) <= diff_limit:
                return True
            else:
                return False
        except:
            return False

    def postDataScrapper(self, postsList):

        print("post-scrapping")

        postDetails = {}

        hash_list = []

        for x in postsList:
            y = 'https://www.instagram.com/p/' + x + '/'

            postDetails[x] = {}

            postDetails[x]["link"] = y

            self.driver.get(y)

            time.sleep(5)

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            content = self.driver.execute_script("return document.body.innerHTML;")

            postDetails[x]["postTime"] = content.split('datetime="')[-1].split('"')[0]

            postDetails[x]["account"] = \
                content.split('<a class="sqdOP yWX7d     _8A5w5   ZIAjV " href="')[1].split("</a>")[0].split(
                    'tabindex="0">')[1]

            soup = BeautifulSoup(content, features="lxml")
            hash_list = []
            for url in soup.find_all('a'):
                tags = url.get('href')
                if "/explore/tags/" in tags:
                    hash_list.append(tags.split("/explore/tags/")[1][0:-1])
            postDetails[x]["hash"] = hash_list
        tag_bucket.addHashList(postDetails)
        ref.update(postDetails)
        # print(postDetails)


def time_retrive(content):
    l = []
    for i, j in content:
        l.append(j['postTime'])
    l.sort()
    for k in l:
        for i, j in content:
            if j['postTime'] == k:
                main[i] = j

    return main


def generateHTML(post_Details):
    innerHTML = ""
    for post in post_Details.keys():
        innerHTML += '<a class="card" href="#"><span class="card-header"><iframe src = "' + post_Details[post][
            "link"] + 'embed"></iframe></span><span class="card-summary"> Account Name : ' + post_Details[post][
                         "account"] + '<br><hr>Posted:<p>' + post_Details[post]["postTime"] + '</p></span></a>'

    pass

test = pyspeedtest.SpeedTest("www.youtube.com")
tag_bucket = hashQueue({"samsungleaks": 1, "samsungfan": 1})
print(test.download())
agent1 = agent(20)
# agent2 = agent(2)


"""
https://instagram.fcok7-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/261363520_617741472983801_7137038581435344437_n.jpg?_nc_ht=instagram.fcok7-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=7P6ZP1bVExEAX8x_OeR&edm=AP_V10EBAAAA&ccb=7-4&oh=8417c7a4b6402d9220c82ebbaed0d083&oe=61AF53C8&_nc_sid=4f375e
"""