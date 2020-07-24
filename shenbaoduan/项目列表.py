#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 15:25
# file: 项目列表.py
import logging

import requests
import json

from shenbaoduan.申报端登录 import Login


class ProjectList:
    def get_projectlist(self):
        r = requests.get('http://djztec.f3322.net:81/estimate/report/index?page=1',
                         headers={'token':Login.get_token(), 'userid':'99'}
                         ).json()
        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
        return r

    def test_getprojectlist(self):
        r = self.get_projectlist()
        assert r['code'] == 0 and r['msg'] == '项目列表'


p = ProjectList()
p.test_getprojectlist()