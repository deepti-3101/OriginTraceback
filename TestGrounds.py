import requests
from PIL import Image
import imagehash
import pandas as pd
import ipyplot

images = ['https://i.ebayimg.com/images/g/vOUAAOSwVHle64yO/s-l1600.jpg',
         'https://i.ebayimg.com/images/g/jN8AAOSwxMle64yY/s-l1600.jpg',
         'https://i.ebayimg.com/images/g/3p8AAOSwk2Je64ym/s-l1600.jpg',
         'https://i.ebayimg.com/images/g/qqYAAOSweNle64zN/s-l1600.jpg',
         'https://i.ebayimg.com/images/g/cnkAAOSw~n9e64za/s-l1600.jpg',
         'https://i.ebayimg.com/images/g/3p8AAOSwk2Je64ym/s-l64.jpg',
         'https://i.ebayimg.com/images/g/qqYAAOSweNle64zN/s-l64.jpg']

ipyplot.plot_images(images)

df = pd.DataFrame(columns=['image', 'ahash', 'phash', 'dhash', 'whash', 'colorhash'])

for url in images:
    file = Image.open(requests.get(url, stream=True).raw)

    data = {
        'image': url,
        'ahash': imagehash.average_hash(file),
        'phash': imagehash.phash(file),
        'dhash': imagehash.dhash(file),
        'whash': imagehash.whash(file),
        'colorhash': imagehash.colorhash(file),
    }

    df = df.append(data, ignore_index=True)

print(df)
print()
print(df.dhash.duplicated())
print()
print(df.whash.duplicated())
print()
print(df.colorhash.duplicated())
