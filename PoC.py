from PIL import Image
import imagehash
import numpy as np


def sim(similarity, hash1, hash2):
    threshold = 1 - similarity / 100
    diff_limit = int(threshold * (8 ** 2))
    if np.count_nonzero(hash1 != hash2) <= diff_limit:
        print("Images Similar with accuracy upto : " + str(similarity) + "%")
    else:
        print("Images not Similar with the given accuracy: " + str(similarity) + "%")


original = input("Enter the Original Image : ")
check = input("Enter the image to be checked : ")

with Image.open(original) as imgOri:
    hashOri = imagehash.average_hash(imgOri, 8).hash
    print(hashOri)
print("\n\n=-=-=-=-=-=-=-=-==-=-=-=-=-===\n\n")
with Image.open(check) as imgCK:
    hashCK = imagehash.average_hash(imgCK, 8).hash
    print(hashCK)

print("\n\n=-=-=-=-=-=-=-=-==-=-=-=-=-===\n\n")

sim(80, hashOri, hashCK)
