from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

username = "dummyaccount"
password = "2353463463"     # Be careful, don't accidentally expose your password


def login():
    time.sleep(1)

    # maximize the window size
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
    time.sleep(4)


driver = webdriver.Chrome("D:\Python\chromedriver")

products = []
driver.get('https://www.instagram.com/explore/tags/iphone13/')

time.sleep(15.4)

content = driver.page_source

soup = BeautifulSoup(content, features="lxml")

for link in soup.find_all('a'):
    name = link.get('href')
    products.append(name)

df = pd.DataFrame({'Product Name': products})

df.to_csv('products1.csv', index=False, encoding='utf-8')
