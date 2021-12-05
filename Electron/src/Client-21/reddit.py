import praw
from os.path import isfile, join
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import time
from os import listdir
import os
import requests
from PIL import Image
import imagehash
import numpy as np

cred = credentials.Certificate("fb.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-genesis-21-default-rtdb.firebaseio.com/'
})

ref = db.reference('/searchTest4/')

Path("D:/Genesis-21/Searches").mkdir(parents=True, exist_ok=True)

target = "C:\\tmp\\5.jpg"

name = "D:/Genesis-21/Searches"


def hashProbe(threshold, original, data):
    print("IN HASHPROBE")
    targetListFile = open(name + "/test.txt", "a")
    with Image.open(original) as imgOri:
        hash1 = imagehash.average_hash(imgOri, 8).hash
    path = "C:\\tmp\\Genesis-21\\"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    pList = []
    postDetails = {}
    for x in files:
        if sim(threshold, hash1, x):
            if ".jpg" in x:
                x = x.split(".jpg")[0]
            if ".png" in x:
                x = x.split(".png")[0]
            else:
                x = x.split(".gif")[0]
            url = ""
            try:
                url = data[x]["id"]
            except:
                pass
            pList.append(url)
            postDetails[x] = posts[x]
            targetListFile.write(url)
    print(pList)

    if len(postDetails) > 0:
        ref.update(postDetails)
    targetListFile.close()
    return pList


def download(pack):
    print("Downloading")
    for x in pack.keys():
        while True:
            if ".jpg" in pack[x]["img"]:
                ext = ".jpg"
            elif ".png" in pack[x]["img"]:
                ext = ".png"
            else:
                ext = ".gif"

            filename = "C:\\tmp\\Genesis-21\\" + x + ext
            file_exists = os.path.isfile(filename)

            if not file_exists:
                with open(filename, 'wb+') as handle:
                    response = requests.get(pack[x]["img"], stream=True)
                    if not response.ok:
                        print(response)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
            else:
                continue
            break
    hashProbe(82, target, posts)


def sim(similarity, hash1, img2):
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


reddit = praw.Reddit(
    client_id="MoZEYBH36AiOYgjJx5Okqg",
    client_secret="tEXoXdmzvu32dgDAykqJagW2Wz4Rqw",
    user_agent="my user agent",
)

subreddit = reddit.subreddit("repost")

posts = {}
count = 0
for submission in subreddit.hot(limit=500):
    print(count)
    count += 1
    if "i.redd.it" in submission.url:
        posts[submission.id] = {"img": submission.url, "title": submission.title, "id": submission.id,
                                "postTime": submission.created}


x = hashProbe(89, target, posts)

new = {}

for i in x:
    new[i] = posts[i]

print(new)