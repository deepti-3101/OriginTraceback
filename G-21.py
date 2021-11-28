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
from os.path import isfile, join

username = "************"
password = "************"  # Be careful, don't accidentally expose your password wnen commiting 


def hashProbe(threshold, original):
    path = "C:\\tmp\\Genesis-21\\"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    pList = []
    for x in files:
        if sim(threshold, original, x):
            pList.append(x)
    print(pList)


def login(driver):
    time.sleep(1)

    driver.maximize_window()

    # navigate to the url
    driver.get("https://www.instagram.com/")
    time.sleep(4)

    # finds the username box
    usern = driver.find_element_by_name("username")
    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = driver.find_element_by_name("password")

    # sends the entered password
    passw.send_keys(password)

    time.sleep(2)

    # finds the login button
    log_cl = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    log_cl.click()  # clicks the login button
    time.sleep(14)
    ntnow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")
    ntnow.click()


def initScrapper(tag, timeLimit):

    options = Options()
    options.page_load_strategy = 'eager'

    driver = webdriver.Chrome("D:\Python\chromedriver", options=options)

    posDic = {}

    products = []
    posts = []

    time.sleep(10.4)

    login(driver)

    time.sleep(10.4)

    driver.get('https://www.instagram.com/explore/tags/' + tag + '/')

    time.sleep(5.4)

    for i in range(int(timeLimit)):
        time.sleep(4)
        print(i)
        driver.execute_script("window.scrollTo(0,150)")

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        content = driver.execute_script("return document.body.innerHTML;")

        soup = BeautifulSoup(content, features="lxml")

        for link in soup.find_all('a'):
            name = link.get('href')
            if "/p/" in name and name not in products:
                products.append(name.split("/p/")[1].split("/")[0])

        for link in soup.find_all('img'):
            name = link.get('src')
            try:
                if "fbcdn.net/v" in name and "2885-19" not in name and name not in posts:
                    posts.append(name)
            except:
                df = pd.DataFrame({'links': products})
                df1 = pd.DataFrame({'photo': posts})

                df.to_csv('products4.csv', index=False, encoding='utf-8')
                df1.to_csv('posts4.csv', index=False, encoding='utf-8')

    df = pd.DataFrame({'links': products})
    df1 = pd.DataFrame({'photo': posts})

    df.to_csv('products4.csv', index=False, encoding='utf-8')
    df1.to_csv('posts4.csv', index=False, encoding='utf-8')

    if len(posts) == len(products):
        for x in range(len(posts)):
            posDic[products[x]] = posts[x]

        return download(posDic)

    else:
        print("Didn't match")
        print(len(posts), len(products))
        if len(posts) <= len(products):
            for x in range(len(posts)):
                posDic[products[x]] = posts[x]
        else:
            for x in range(len(products)):
                posDic[products[x]] = posts[x]

    f = open("jsonLog.txt", "w")
    f.write(str(posDic))
    f.close()

    return download(posDic)


def download(pack):
    for x in pack.keys():
        while True:
            filename = "C:\\tmp\\Genesis-21\\" + x + ".jpg"
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


def sim(similarity, img1, img2):
    with Image.open(img1) as imgOri:
        hash1 = imagehash.average_hash(imgOri, 8).hash
    with Image.open("C:\\tmp\\Genesis-21\\" + img2) as imgCK:
        hash2 = imagehash.average_hash(imgCK, 8).hash
    threshold = 1 - similarity / 100
    diff_limit = int(threshold * (8 ** 2))
    if np.count_nonzero(hash1 != hash2) <= diff_limit:
        print(True)
        return True
    else:
        print(False)
        return False



#initScrapper("dolittlemovie", 50)
hashProbe(80, "C:\\tmp\\B3iMTb9lcfY.jpg")
