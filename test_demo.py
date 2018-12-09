#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest





def test_zero_division():
    print 'test'
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)