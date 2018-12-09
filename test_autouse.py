#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
fixture decorator一个optional的参数是autouse, 默认设置为False。
当默认为False，就可以选择用上面两种方式来试用fixture。
当设置为True时，在一个session内的所有的test都会自动调用这个fixture。
'''


import time
import pytest

@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')

def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')
