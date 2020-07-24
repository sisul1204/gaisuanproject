#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 16:52
# file: 获取列表.py
import json
import logging

import requests

from shenheduan.审核登录 import Login


class GetList:

    def get_projectlist(self):
        r = requests.get('http://djztec.f3322.net:81/web2/project/list',
                         headers={'token':Login.get_token(), 'userid':'83'},
                         params={'project_name':'', 'status': '2'}
                         ).json()

        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))

        return r

    def test_get_projectlist(self):
        r = self.get_projectlist()
        print(r)

lst = GetList().test_get_projectlist()