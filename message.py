import requests
import json
import os
import time


def dingtalk(msg, dingtalk_token, tries=5):
    dingtalk_url = 'https://oapi.dingtalk.com/robot/send?access_token='+dingtalk_token
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "isAtAll": False
        }
    }
    header = {'Content-Type': 'application/json'}

    for _ in range(tries):
        try:
            r = requests.post(dingtalk_url,
                              data=json.dumps(data), headers=header).json()
            print(r)
            if r["errcode"] == 0:
                return True
        except:
            pass
        print('Retrying...')
        time.sleep(5)
    return False

if __name__ == "__main__":
    msg = "打卡"*1000
    dingtalk_token = os.environ.get('DINGTALK_TOKEN')
    if dingtalk_token:
        ret = dingtalk(msg, dingtalk_token)
        print('send_dingtalk_message', ret)
