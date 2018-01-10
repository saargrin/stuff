#!/usr/bin/python
import urllib
import PIL
from PIL import ImageFile
import sys
import json
from pprint import pprint
import csv

    
def getsizes(uri):
    file = urllib.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size
            break
    file.close()
    return size, None

out = open("output.csv","a")
fieldnames = ['NASA_ID','Size']
writer = csv.DictWriter(out,fieldnames=fieldnames)
writer.writeheader()

data = json.load(open(sys.argv[1]))
for item in data["collection"]["items"]:
 file = urllib.urlopen(item["href"])
 meta = json.load(file)
 url = meta[0]
 id  = item["data"][0]["nasa_id"] 
 print id
 size = getsizes (url)
 writer.writerow({'NASA_ID':id,'Size':size})

