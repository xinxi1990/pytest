#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示依赖关系
'''


import pytest

@pytest.mark.run('second-to-last')


# @pytest.mark.order1
# def test_1():
#     print "test_1th"
#     assert True
#
# @pytest.mark.order2
# def test_2():
#     print "test_2th"
#     assert True



@pytest.mark.run('second-to-last')
def test_three():
    assert True

@pytest.mark.run('last')
def test_four():
    assert True

@pytest.mark.run('second')
def test_two():
    assert True

@pytest.mark.run('first')
def test_one():
    assert True



import pytest

@pytest.mark.run(order=-2)
def test_three():
    assert True

@pytest.mark.run(order=-1)
def test_four():
    assert True

@pytest.mark.run(order=2)
def test_two():
    assert True

@pytest.mark.run(order=1)
def test_one():
    assert True