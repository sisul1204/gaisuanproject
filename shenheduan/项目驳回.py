#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 17:18
# file: 项目驳回.py
import requests

from shenheduan.认领项目 import ClaimProject


class RejectProject:
    def rejectproject(self):
        r = ClaimProject().claimproject()
        estimate_id = r['result']['list'][0]['id']
        print('&'*100)
        print(estimate_id, type(estimate_id))
        r = requests.post('http://djztec.f3322.net:81/web2/project/reject',
                          data={'estimate_id':estimate_id, 'remark':'缺少文件','img':'shenheduan/homework.gif'},
                          headers={'content-type':'multipart/form-data'}
                          ).json()

        return r

    def test_rejectproject(self):
        r = self.rejectproject()
        assert r['code'] == 0 and r['msg'] == 'success'

reject = RejectProject()
reject.test_rejectproject()