#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 10:06
# file: 申报端登录.py
import json
import logging

import requests


class Login:
    logging.basicConfig(level=logging.DEBUG)
    url = 'http://djztec.f3322.net:81/declare/loginuser'
    # data = {'username':'test9527', 'password':'111111'}
    @classmethod
    def get_token(cls):
        r = requests.post(Login.url,
                          json = {'username':'test9527','password':'111111'},
                          headers = {'content-type':'application/json'}
                          ).json()
        # logging.info(json.dumps(r, indent=2, ensure_ascii=False))
        assert r['code'] == 0 and r['message'] == '登录成功'
        print(r['result']['token'])
        return r['result']['token']

login = Login()
login.get_token()