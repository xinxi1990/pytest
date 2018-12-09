#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示标签分组

pytest test_marks.py -m=webtest -s 跑webtest标签

pytest test_marks.py -m "not webtest" -s 跑不包含webtest标签
'''
import pytest

@pytest.mark.webtest
def test_send_http():
    print "test_send_http"

@pytest.mark.webtest
def test_something_quick():
    print "test_something_quick"

def test_another():
    print "test_another"

class TestClass:
    def test_method(self):
        pass

if __name__ == "__main__":
    pytest.main(["-s", "test_server.py", "-m=webtest"])





