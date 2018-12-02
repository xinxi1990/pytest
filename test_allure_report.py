#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示用allure生成报告
'''
import allure
import pytest
import json
users = json.loads(open('./users.test.json', 'r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        print "passwd is:{}".format(passwd)
        assert len(passwd) >= 6
        msg = "user %s has a weak password" %(user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg