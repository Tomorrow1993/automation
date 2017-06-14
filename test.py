#coding=utf8
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.yinwang.org')
soup = BeautifulSoup(r.text,"html.parser")
a = soup.select(".list-group-item a")
print a[0].string
print a[0].attrs["href"]





