#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
演示pytest-selenium插件
pytest --driver Firefox -k test_example
https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
'''
import pytest,json,time
from pytest_selenium import selenium
from pytest_selenium import driver

# @pytest.fixture
# def driver_args():
#     return ['--log-level=LEVEL']


def test_selenium(selenium):
    selenium.get('http://www.baidu.com')
    time.sleep(3)
    #driver.find_element(By.XPATH,'//*[@id="u1"]/a[3]').click()



