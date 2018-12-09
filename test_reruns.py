#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示失败重试
'''

import pytest

@pytest.mark.flaky(reruns=5)
def test_example():
    #import random
    #assert random.choice([True, False])
    assert 1 == 2



@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example():
    # import random
    # assert random.choice([True, False])
    assert 1 == 2