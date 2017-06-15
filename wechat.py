# coding=utf8
import itchat
import net
import tuling

tuling_anable = False  # 是否开启图灵机器人


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    global tuling_anable
    if msg['ToUserName'] != 'filehelper': return
    content = msg['Text'].strip()
    if content == 'start':
        tuling_anable = True
        itchat.send(u'已开启图灵机器人', 'filehelper')
    elif content == 'end':
        tuling_anable = False
        itchat.send(u'已关闭图灵机器人', 'filehelper')
    elif tuling_anable:
        itchat.send(tuling.tuling(content, msg['ToUserName']), 'filehelper')
    elif 'blog' in content:
        if 'list' in content:
            itchat.send(net.get_yw_blog_list(), 'filehelper')
        else:
            itchat.send(net.get_yw_blog(), 'filehelper')
    elif content == 'help':
        itchat.send(buildHelpMessage(), 'filehelper')
    else:
        itchat.send(buildHelpMessage(), 'filehelper')


def buildHelpMessage():
    return u"目前支持功能:\n" \
           + u"blog:--->获取王垠最新博客\n" \
           + u"blog list:--->获取王垠所有博客\n" \
           + u"start/end:--->开启/关闭图灵机器人问答"


itchat.auto_login(hotReload=True, enableCmdQR=2)

itchat.send(u'输入help,显示帮助信息', 'filehelper')
itchat.run()
