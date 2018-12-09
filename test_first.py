#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
第一个入门演示

• 测试文件以 test_ 开头(以 _test 结尾也可以)
• 测试类以 Test 开头，并且不能带有 __init__ 方法
• 测试函数以 test_ 开头
'''


import pytest

@pytest.mark.P2
def test_zero_division():
    print '====test_zero_division===='
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    print '====test_recursion_depth===='
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)


def test_fail():
    print '====test_fail====='
    assert 1 == 2