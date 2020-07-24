#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/24 11:08
# file: 项目添加.py
import logging
import time

import requests
import json
import pystache
from faker import Faker

from shenbaoduan.申报端登录 import Login


class AddProject:
    uid = str(time.time())
    faker = Faker(locale='zh_CN')
    def addproject_template(self):
        data = self.get_project({'project_name':AddProject.faker.company(),'address':AddProject.faker.address(),'wenhao':AddProject.faker.bban(), 'project_num':AddProject.faker.ean(length=13)})
        print(data)
        print(type(data))
        data = json.loads(data, encoding='utf-8')
        print(type(data))
        # data = data.encode('utf-8')

        r = requests.post('http://djztec.f3322.net:81/estimate/report',
                          data=data,
                          headers={'token':Login.get_token(),'userid':'99',
                                   'content-type':'application/x-www-form-urlencoded;charset=UTF-8'}

                          # proxies={'http':'127.0.0.1:8888'}
                          ).json()
        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
        return r


    def test_addproject_template(self):
        r = self.addproject_template()
        assert r['code'] == 0 and r['msg'] == '添加成功'



    def get_project(self,dct):
        template = ''.join(open('project.json', encoding='utf-8').readlines())
        return pystache.render(template, dct)

    def test_get_project(self):
        logging.debug(self.get_project({'project_name':'测试项目'+AddProject.uid,'address':'西湖区','wenhao':AddProject.uid, 'project_num':AddProject.uid}))

addproject = AddProject()
# addproject.test_get_project()
addproject.test_addproject_template()