# coding=utf8
global a
a = (u'filehelper',
     u'@62dc6876da4ec24916b4f7a58e3ad1767b89aff60ce28f8408af88beb19ef0bd',
     u'@350d1cef1b54396ad3c4bdde8cab52f20a6e0e19846a6ba6642a70aa2fbd1c89',
     u'@aac80b951f54b3f66c0d201989211299b6079ec9443dfe9c3c960b0ce278340e',
     u'@d77c8fd4c0a87607ea2a0ec27c510b8b4998be00d49f4529845cd86639af5188')

users = {

}


def tuling_enable(user_name):
    global users
    if user_name in users:  # 如果已经有了
        info = users[user_name]
        if info:
            return info['tuling_enable']
        else:
            return False
    else:
        return False


def toggle_tuling(user_name, toggle):
    global users
    if user_name in users:  # 如果已经有了
        info = users[user_name]
        if info:
            info['tuling_enable'] = toggle
        else:
            info['tuling_enable'] = toggle
    else:
        users[user_name] = {
            'tuling_enable': toggle
        }
