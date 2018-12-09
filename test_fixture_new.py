#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示使用fixture实现,setup和teardown
@pytest.fixture(scope="function") 方法级别
@pytest.fixture(scope="class")   类级别
@pytest.fixture(scope="module") 模块级别
https://docs.pytest.org/en/latest/fixture.html
'''

import time
import pytest


#
# @pytest.fixture(scope="function")
# # @pytest.fixture(scope="module")
# def login():
#     print "before_login"
#     yield
#     print "after_login"

# def test_a(login):
#     print "test_a"


@pytest.fixture(scope="class")
def login():
    print "before_login"
    yield
    print "after_login"


@pytest.mark.usefixtures('login')
def test_a():
    print "test_a"

@pytest.mark.usefixtures('login')
def test_b():
    print "test_b"