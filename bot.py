from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

username = "*************"
password = "*************"  # Be careful, don't accidentally expose your password


def login():
    time.sleep(1)

    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    time.sleep(4)
    usern = driver.find_element_by_name("username")
    usern.send_keys(username)
    passw = driver.find_element_by_name("password")
    passw.send_keys(password)

    time.sleep(2)
    log_cl = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    log_cl.click()
    time.sleep(14)
    ntnow = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")
    ntnow.click()


options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome("D:\Python\chromedriver", options=options)

posDic = {}

products = []
posts = []

time.sleep(10.4)

login()

time.sleep(10.4)


def scrapData(tag, timeLimit):
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
                products.append(name)

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
    else:
        print("Didn't match")
        if len(posts) <= len(products):
            for x in range(len(posts)):
                posDic[products[x]] = posts[x]
        else:
            for x in range(len(products)):
                posDic[products[x]] = posts[x]

    f = open("json.txt", "w")
    f.write(str(posDic))
    f.close()

    con = input("Want to Continue ?")
    if con == "y":
        scrapData(input("Enter the Tag : "), input("Enter the time limit : "))


scrapData(input("Enter the Tag : "), input("Enter the time limit : "))
