#coding=utf8
import itchat
# 这个可以用来主动给手机微信发送一些消息
itchat.auto_login(True)

itchat.send('Hello, filehelper', toUserName='filehelper')