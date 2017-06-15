# coding=utf8
import itchat
import net


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    content = msg['Text'].strip()
    if u'blog' in content:
        if u'list' in content:
            itchat.send(net.get_yw_blog_list(), 'filehelper')
        else:
            itchat.send(net.get_yw_blog(), 'filehelper')
    elif content == u'help':
        itchat.send(buildHelpMessage(), 'filehelper')
    else:
        itchat.send(buildHelpMessage(), 'filehelper')


def buildHelpMessage():
    return u"目前支持功能:\n" + u"blog:--->获取王垠最新博客\n"


itchat.auto_login(hotReload=True, enableCmdQR=2)

itchat.send(u'输入help,显示帮助信息', 'filehelper')
itchat.run()
