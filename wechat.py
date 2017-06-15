# coding=utf8
import itchat
import net
import tuling
import whitelist

tuling_anable = False  # 是否开启图灵机器人


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    global tuling_anable
    user_name = msg['FromUserName']
    # if user_name not in whitelist.a: return
    content = msg['Text'].strip()
    if content == 'start':
        tuling_anable = True
        msg.user.send(u'已开启图灵机器人')
    elif content == 'end':
        tuling_anable = False
        msg.user.send(u'已关闭图灵机器人')
    elif tuling_anable:
        msg.user.send(tuling.tuling(content, user_name[-10:]))
    elif 'blog' in content:
        if 'list' in content:
            msg.user.send(net.get_yw_blog_list())
        else:
            msg.user.send(net.get_yw_blog())
    elif content == 'help':
        msg.user.send(buildHelpMessage())
    else:
        msg.user.send(buildHelpMessage())


def buildHelpMessage():
    return u"目前支持功能:\n" \
           + u"blog:--->获取王垠最新博客\n" \
           + u"blog list:--->获取王垠所有博客\n" \
           + u"start/end:--->开启/关闭图灵机器人问答"


itchat.auto_login(hotReload=True, enableCmdQR=2)

itchat.send(u'输入help,显示帮助信息', 'filehelper')
itchat.run()
