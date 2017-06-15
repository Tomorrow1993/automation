# coding=utf8
import requests
from bs4 import BeautifulSoup


# 获取王垠最新的博客
def get_yw_blog():
    r = requests.get('http://www.yinwang.org')
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.select(".list-group-item a")
    return u"题目：" + a[0].string + "\n" + "http://www.yinwang.org" + a[0].attrs["href"]


def get_yw_blog_list():
    r = requests.get('http://www.yinwang.org')
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.select(".list-group-item a")
    result = ""
    for link in a:
        tem = u"题目：" + link.string + "\n" + "http://www.yinwang.org" + link.attrs["href"] + "\n"
        result = result + tem
    return result
