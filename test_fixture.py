#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示使用fixture实现,setup和teardown
'''

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def chrome_driver(scope="function"):
    """
    scope="function"是scope的默认值，表示这是一个function级别的fixture
    """
    print("setup() begin")
    driver = webdriver.Chrome()
    url = 'http://www.baidu.com'
    driver.get(url)
    print("setup() end")
    yield driver
    #这里会返回driver，给使用这个fixture为参数的test_函数使用，
    #test_函数结束后，会回到这里，继续执行后面语句
    print("teardown() begin")
    driver.close()
    print("teardown() end")


class TestBaiDu(object):

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def test_search_0(self, chrome_driver):
        """
        这里的chrome_driver是在本模块中定义的fixture，这里输入
        的参数是上面yield driver中返回的driver
        """
        chrome_driver.find_element(*self.locator_kw).send_keys(u'selenium 测试')
        chrome_driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = chrome_driver.find_elements(*self.locator_result)
        for link in links:
            print (link.text)