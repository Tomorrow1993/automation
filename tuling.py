# coding=utf8
import requests


def tuling(message, user_id):
    payload = {'key': 'fb1887adcca1464b93e526b412c2c786',
               'userid': user_id,
               'info': message.encode('utf-8'),
               'loc': u'上海'}
    r = requests.post('http://www.tuling123.com/openapi/api', payload)
    if r.status_code == requests.codes.ok:
        return r.json().text
    else:
        return u'万恶的网络又被劫持了'
