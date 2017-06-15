# coding=utf8
import itchat
import net
import tuling


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    content = msg['Text'].strip()
    if 'blog' in content:
        if 'list' in content:
            itchat.send(net.get_yw_blog_list(), 'filehelper')
        else:
            itchat.send(net.get_yw_blog(), 'filehelper')
    elif content == 'help':
        itchat.send(buildHelpMessage(), 'filehelper')
    elif 'ask' in content:
        message = content.split('_', 1)[1]
        itchat.send(tuling.tuling(message, msg['ToUserName']), 'filehelper')
    else:
        itchat.send(buildHelpMessage(), 'filehelper')


def buildHelpMessage():
    return u"目前支持功能:\n" \
           + u"blog:--->获取王垠最新博客\n" \
           + u"blog list:--->获取王垠所有博客\n" \
           + u"ask_问题:--->机器人问答"


itchat.auto_login(hotReload=True, enableCmdQR=2)

itchat.send(u'输入help,显示帮助信息', 'filehelper')
itchat.run()
