# coding=utf8
import requests
import json


def tuling(message, user_id):
    payload = {
        "perception": {
            "inputText": {
                "text": message
            },
            "selfInfo": {
                "location": {
                    "city": u'上海',
                },
            }
        },
        "userInfo": {
            "apiKey": "fb1887adcca1464b93e526b412c2c786",
            "userId": user_id
        }
    }
    try:
        r = requests.post('http://openapi.tuling123.com/openapi/api/v2', json=payload, timeout=8)
        if r.status_code == requests.codes.ok:
            return hand_response(json.loads(r.text))
        else:
            return u'万恶的网络又被劫持了'
    except(requests.exceptions.RequestException):
        return u'万恶的网络又出问题了'


def hand_response(response):
    if response.has_key('results'):
        results = response['results']
        result = ''
        for item in results:
            if item['resultType'] == 'text':
                result += item['values']['text'] + "\n"
            if item['resultType'] == 'url':
                result += item['values']['url'] + "\n"
        return result.rstrip('\n')
    else:
        return u"出了点问题QAQ"
        # code = response['code']
        # if code == 100000:  # 文本类
        #     return response['text']
        # elif code == 20000:  # 链接类
        #     return response['text'] + "\n" + response['url']
        # elif code == 302000:  # 新闻类
        #     return response['text']
        # elif code == 308000:  # 菜谱类
        #     return response['text']
        # else:
        #     return response['text']
