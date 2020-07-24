#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 16:37
# file: 认领项目.py
import json
import logging

import requests

from shenheduan.审核登录 import Login
from shenheduan.获取列表 import GetList


class ClaimProject:
    def claimproject(self):

        estimate_id = GetList().get_projectlist()['result']['list'][0]['id']

        r = requests.post('http://djztec.f3322.net:81/web2/project/claim',
                          data={'estimate_id':estimate_id},
                          headers={'token':Login.get_token(),'userid':'83'}
                          ).json()
        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))

        return r

    def test_claimproject(self):
        r = self.claimproject()
        assert r['code'] == 0 and r['message'] == '认领成功'

claim = ClaimProject()
claim.test_claimproject()

