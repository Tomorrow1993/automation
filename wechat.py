#coding=utf8
import itchat
 
@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(u'帮助信息', 'filehelper')
    else:
        itchat.send(u'其他信息', 'filehelper')

def run():
	itchat.auto_login(hotReload=True,enableCmdQR=2)
	itchat.send(u'输入 帮助,显示帮助信息', 'filehelper') 
	itchat.run()

if __name__ == '__main__':
	run();
