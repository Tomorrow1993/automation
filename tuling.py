# coding=utf8
import requests
import json


def tuling(message, user_id):
    payload = {'key': 'fb1887adcca1464b93e526b412c2c786',
               'userid': user_id,
               'info': message.encode('utf-8'),
               'loc': u'上海'}
    try:
        r = requests.post('http://www.tuling123.com/openapi/api', payload, timeout=8)
        if r.status_code == requests.codes.ok:
            try:
                return hand_response(json.loads(r.text))
            except (ValueError):
                return u'万恶的网络又被劫持了'
        else:
            return u'万恶的网络又被劫持了'
    except(requests.exceptions.RequestException):
        return u'万恶的网络又出问题了'


def hand_response(response):
    code = response['code']
    if code == 100000:  # 文本类
        return response['text']
    elif code == 20000:  # 链接类
        return response['text'] + "\n" + response['url']
    elif code == 302000:  # 新闻类
        return response['text']
    elif code == 308000:  # 菜谱类
        return response['text']
    else:
        return response['text']
