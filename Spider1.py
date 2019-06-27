# -*- coding: utf-8 -*-
import os
import re
import requests
import requests as requests
from bs4 import BeautifulSoup

_url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
urls = [_url.format(page=page) for page in range(1, 4328+1)]
url = urls[0]

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
img_list = soup.find_all('img', class_='ui image lazy')

path = "F:\\image\\"

for img in img_list:
       image = img.get('data-original')
       title = img.get('title')
       title = re.sub(r'\W', '', title)
       # print(image)
       with open(path + title + os.path.splitext(image)[-1], 'wb') as f:
            img = requests.get(image).content
            f.write(img)
