#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
演示用unittest执行并生成报告
'''
import unittest,os,time,sys
from HTMLTestRunner import HTMLTestRunner
import logging
reload(sys)
sys.setdefaultencoding('utf8')


logging.basicConfig(filename='logger.log', level=logging.INFO)
logger = logging.getLogger("unittest:")


def setUpModule():
    print("setUpModule >>>")



class UNIT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # logger.info("setUpClass")
        print "setUpClass"


    def setUp(self):
        print "setUp"


    def test_1(self):
        print "test_1"

    def tearDown(self):
        print "tearDown"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"


def tearDownModule():
    print("tearDownModule >>>")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UNIT("test_1"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = os.getcwd() + '/result.html'
    print filename
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况:')
    runner.run(suite)
    fp.close()  # 关闭报告文件
