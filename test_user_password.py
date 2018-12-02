#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示多个
'''

import pytest
import json

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read()) # 读取当前路径下的users.dev.json文件，返回的结果是dict

    def test_user_password(self, users):
        # 遍历每条user数据
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123', msg