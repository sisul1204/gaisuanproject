#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 16:38
# file: 审核登录.py
import json
import logging

import requests


class Login:
    logging.basicConfig(level=logging.DEBUG)
    url = 'http://djztec.f3322.net:81/approval/loginuser'
    @classmethod
    def get_token(self):
        r = requests.post(Login.url,
                          json={'username': 'lizhipeng', 'password': '111111'},
                          headers={'content-type': 'application/json'}
                          ).json()

        # logging.debug(json.dumps(r,indent=2,ensure_ascii=False))

        return r['result']['token']

result = Login().get_token()
assert len(result) != 0

