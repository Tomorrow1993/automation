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
            print r.text
            return json.loads(r.text)['text']
        else:
            return u'万恶的网络又被劫持了'
    except(requests.exceptions.RequestException):
        return u'万恶的网络又出问题了'
