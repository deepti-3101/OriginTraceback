import os
import requests
from PIL import Image
import imagehash
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from os import listdir
from os.path import isfile, join
from collections import OrderedDict
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


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
        print("Queue status : ")
        self.nextHash(0)

    def nextHash(self, mode):
        sort_orders = sorted(self.pQueue.items(), key=lambda x: x[1], reverse=True)
        ref.update({"pQueue": sort_orders})
        if len(sort_orders) >= 0:
            print(sort_orders)
            current = sort_orders[0][0]
            if mode == 1:
                self.processed.append(current)
                self.assignHash(current)
                return current
            else:
                return sort_orders
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


def time_retrive(content):
    l = []
    m = []
    main = {}
    for i in content:
        l.append(content[i])
    for j in l:
        m.append(j['postTime'])
    m.sort()
    for i in m:
        for j in content:
            value = content[j]
            if i == value['postTime']:
                main[j] = value

    return main


class agent:
    options = Options()

    options.add_argument("--headless")

    options.page_load_strategy = 'eager'

    posDic = {}

    products = []

    m = input("Enter Mode : ")

    if m == "1":
        driver = webdriver.Chrome("D:\Python\chromedriver", options=options)
    else:
        driver = webdriver.Chrome("chromedriver", options=options)

    posts = []

    fetch = 0

    def __init__(self, fetch1):
        print("Fetch frequency : ", fetch1)
        self.fetch = fetch1
        self.clearWorkSpace()
        self.login()

    def clearWorkSpace(self):
        path = workingDirectory
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for x in files:
            os.remove(path + x)

    def hashProbe(self, threshold, original):
        print("IN HASHPROBE")
        targetListFile = open(name + "/test.txt", "a")
        with Image.open(original) as imgOri:
            hash1 = imagehash.average_hash(imgOri, 8).hash
            print(hash1)
        path = workingDirectory
        files = [f for f in listdir(path) if isfile(join(path, f))]
        pList = []
        for x in files:
            print(x)
            if self.sim(threshold, hash1, x):
                url = x.split(".jpg")[0]
                pList.append(url)
                targetListFile.write(url)
        print(pList)
        self.postDataScrapper(pList)
        targetListFile.close()

    def login(self):
        print("Loggin in ")
        time.sleep(5 - timespeed)

        self.driver.maximize_window()

        # navigate to the url
        self.driver.get("https://www.instagram.com/")
        time.sleep(4 - timespeed)
        try:
            # finds the username box
            usern = self.driver.find_element_by_name("username")
            # sends the entered username
            usern.send_keys(username)
            # finds the password box
            passw = self.driver.find_element_by_name("password")

            # sends the entered password
            passw.send_keys(password)

            time.sleep(4 - timespeed)

            self.driver.execute_script('document.getElementsByClassName("sqdOP  L3NKy   y3zKF     ")[0].click()')
            # clicks the login button
            time.sleep(5 - timespeed)
        except:

            print("Already Logged in - Exception occurred")

        self.initScrapper(tag_bucket.nextHash(1), self.fetch)

    def initScrapper(self, tag, timeLimit):

        print("Init Scrapper")

        self.posts = []

        self.posDic = {}

        time.sleep(5.4 - timespeed)

        self.driver.execute_script('location.replace("https://www.instagram.com/explore/tags/' + tag + '/")')

        time.sleep(5.4 - timespeed)

        for i in range(int(timeLimit)):

            time.sleep(6 - timespeed)

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
                    print("Exception when getting link")
                    pass
                if "/p/" in name1 and name1 not in self.products:
                    self.products.append(name1)

            for link in soup.find_all('img'):
                name1 = link.get('src')
                try:
                    if "fbcdn.net/v" in name1 and "2885-19" not in name1 and name1 not in self.posts:
                        self.posts.append(name1)
                except:
                    print("Exception Occurred when getting image")

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
        print("Length : ", len(pack))
        for x in pack.keys():
            while True:
                filename = workingDirectory + x[:-1] + ".jpg"
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
            with Image.open(workingDirectory + img2) as imgCK:
                hash2 = imagehash.average_hash(imgCK, 8).hash
            threshold = 1 - similarity / 100
            diff_limit = int(threshold * (8 ** 2))
            if np.count_nonzero(hash1 != hash2) <= diff_limit:
                print("yes")
                return True
            else:
                print("no")
                return False
        except:
            print("no")
            print("exception occured when finding similarity")
            return False

    def postDataScrapper(self, postsList):

        print("post-scrapping")

        postDetails = {}

        for x in postsList:

            print("Scrapping : " + x)

            y = 'https://www.instagram.com/p/' + x + '/'

            postDetails[x] = {}

            postDetails[x]["link"] = y

            self.driver.get(y)

            time.sleep(5)

            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            content = self.driver.execute_script("return document.body.innerHTML;")

            postDetails[x]["postTime"] = content.split('datetime="')[-1].split('"')[0]

            postDetails[x]["des"] = "OCR : "

            ocr = content.split('" class="FFVAD"')

            postDetails[x]["des"] += ocr[0].split('<img alt="')[1] + " "

            if "tagging" in postDetails[x]["des"]:

                tagginglist = []

                for tags in postDetails[x]["des"].split("tagging ")[1].split(" "):

                    if "@" in tags:
                        tagginglist.append(tags[:-1])

                postDetails[x]["tags"] = tagginglist

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

        if len(postDetails) > 0:
            ref.update({"postdetails" : postDetails})
            for i in time_retrive(postDetails):
                print(i)
                ref1.update({"origin": i})
                ref.update({"origin": i})
                break
            tag_bucket.addHashList(postDetails)
            self.routeSearch(tag_bucket.nextHash(0))
        else:
            print("Nothing Found")
            ref.update({"Status": "Completed"})
            print("\n=================\nSearch Terminated\n=================\n")
        # print(postDetails)

    def routeSearch(self, search_list):
        if search_list[0][1] > 1:
            print("Routing Search to : ", search_list[0][0], "\n\n")
            self.clearWorkSpace()
            self.initScrapper(tag_bucket.nextHash(1), fetch)
        else:
            ref.update({"Status": "Completed"})
            print("\n=================\nSearch Terminated\n=================\n")


def generateHTML(post_Details):
    innerHTML = ""
    for post in post_Details.keys():
        innerHTML += '<a class="card" href="#"><span class="card-header"><iframe src = "' + post_Details[post][
            "link"] + 'embed"></iframe></span><span class="card-summary"> Account Name : ' + post_Details[post][
                         "account"] + '<br><hr>Posted:<p>' + post_Details[post]["postTime"] + '</p></span></a>'
    pass


cred = credentials.Certificate("fb.json")

timespeed = 0

project_name = input("Enter Project Name : ")

workingDirectory = input("Enter Working Directory (example : D:\\tmp\\Genesis-21\\): ")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-genesis-21-default-rtdb.firebaseio.com/'
})

ref = db.reference('/results/iphone14')

ref1 = db.reference('networks/stream/active')

ref.update({"Status": "Initiated"})

Path("D:/Genesis-21/Searches").mkdir(parents=True, exist_ok=True)

username = "dem.odummy"
password = "orproject5"  # Be careful, don't accidentally expose your password when committing
name = "D:/Genesis-21/Searches"
target = input("Target Image Location (D:\\tmp\\1234.jpg) : ")
main = OrderedDict()

readParameter = ref1.get()

time.sleep(5 - timespeed)

print(readParameter["hashtag"])

tag_bucket = hashQueue({readParameter["hashtag"]: 1})

fetch = readParameter["fetch"]
