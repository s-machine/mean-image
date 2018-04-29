###########################################################################
####This file goes to a link, and scrapes certain images from the file#####
#############Too many customization so didn't make a function##############
##############################Samson Liu###################################

import re
import requests
import urllib.request
import urllib.error
import os, os.path

handler=urllib.request.HTTPCookieProcessor(cookie)
#create an opener
opener = urllib.request.build_opener(handler)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }

categories = ["BEVERAGE", "DESSERT", "PORK"]

base_url = "http://www.laurainthekitchen.com/recipe-category.php?category="
base_img_url = "http://www.laurainthekitchen.com/"

for category in categories:
    url = base_url + category
    #pull up a page
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)


    content = response.read().decode('utf-8')
    pattern = re.compile(r'(?<=img src=")\S*(?<!")', re.S)
    items = re.findall(pattern, content)

    if not os.path.exists(str(category)):
        os.mkdir(str(category))

    for i in range(0, len(items)):
        #we don't want the logo
        if items[i] == "logo.png": continue
        #full image url
        imgUrl = base_img_url+items[i]
        print(imgUrl)
        try:
            urllib.request.urlretrieve(imgUrl, os.path.join(str(category), str(i) +".jpg"))
        except urllib.error.HTTPError: # 404, 500, etc..
            print("Not exist!")