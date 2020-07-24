#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 15:47
# file: 项目撤回.py
import requests

from shenbaoduan.申报端登录 import Login
from shenbaoduan.项目列表 import ProjectList
from shenbaoduan.项目添加 import AddProject


class ProjectRevoke:
    def get_revoke_project(self):
        AddProject().addproject_template()
        lst = ProjectList().get_projectlist()

        id = lst['result']['data'][0]['id']
        print(id)
        url = 'http://djztec.f3322.net:81/estimate/report/{}/revoke'.format(id)
        r = requests.post(url,
                         headers={'token':Login.get_token(), 'userid':'99'},
                         ).json()
        return r

    def test_get_revoke_project(self):
        r = self.get_revoke_project()
        assert r['code'] == 0 and r['msg'] == '撤回成功'

pr = ProjectRevoke()
pr.test_get_revoke_project()





