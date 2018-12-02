#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示参数化多个参数
'''


import pytest
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected