#coding=utf8
import itchat
import requests
from bs4 import BeautifulSoup
@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'].strip() == u'blog':
		itchat.send(getYWBlog(), 'filehelper')
    elif msg['Text'].strip() == u'help':
		itchat.send(buildHelpMessage(), 'filehelper')
    else:
    	itchat.send(buildHelpMessage(), 'filehelper')


def getYWBlog():
	r = requests.get('http://www.yinwang.org')
	soup = BeautifulSoup(r.text,"html.parser")
	a = soup.select(".list-group-item a")
	return u"题目："+a[0].string+"\n"+"http://www.yinwang.org"+a[0].attrs["href"]

def buildHelpMessage():
	return u"目前支持功能:\n"+u"blog:--->获取王垠最新博客\n"


def lc():
    print('finish login')
def ec():
    print('exit')
    
itchat.auto_login(hotReload=True,enableCmdQR=False,loginCallback=lc, exitCallback=ec)
itchat.send(u'输入help,显示帮助信息', 'filehelper') 
itchat.run()
