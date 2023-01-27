import re
import urllib.request
import os
import math
from collections import Counter

#album_url = "https://imgur.com/a/LsAQkBz"
album_url = "https://imgur.com/a/imgururl"



match = re.search("(https?)://(www.)?(?:m.)?imgur.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", album_url)
album_key = match.group(4)

fullListURL = "https://imgur.com/a/" + album_key + "/layout/blog"

response = urllib.request.urlopen(fullListURL)
html = response.read().decode()
imageIDs = re.findall(r'"hash":"([a-zA-Z0-9]+)"', html)

cnt = Counter()
for i in imageIDs:
    cnt[i[1]] += 1

albumFolder = album_key

if not os.path.exists(albumFolder):
    os.makedirs(albumFolder)

for (counter, image) in enumerate(imageIDs, start=1):
    image_url = "https://i.imgur.com/"+image+".jpg"
    prefix = "%0*d-" % (int(math.ceil(math.log10(len(imageIDs)))), counter)
    destination = albumFolder + "/" + image + ".jpg"
    urllib.request.urlretrieve(image_url, destination)
print(cnt.keys)
print(cnt.most_common())
print("The images have been downloaded to "+albumFolder)



