#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
演示使用assume插件
一个pytest插件，允许每次测试多次失败
'''


import pytest

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(True)
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)
