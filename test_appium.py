#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
演示Appium自动化,使用fixture机制
'''
import pytest,os,subprocess,time
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from loggers import JFMlogging
logger = JFMlogging().getloger()

class CreatAppiumDriver(object):
    driver = None
    def  __init__(self ,device,pck_name,lanuch_activity):
        self.device = device
        self.url = "127.0.0.1"
        self.port = "4723"
        self.pck_name = pck_name
        self.lanuch_activity = lanuch_activity
        self.appium_log = './appium.log'

    def init_capability(self):
        '''
        启动配置文件
        :return:
        '''
        desired_caps = {
            "platformName": "Android",
            "appPackage": self.pck_name,
            "platformVersion ": "7.0",
            "appActivity": self.lanuch_activity,
            "autoLaunch": "true",
            "unicodeKeyboard": "true", # 使用appium的输入法，支持中文并隐藏键盘
            "resetKeyboard": "true", # 重置键盘
            "newCommandTimeout": 120, # 设置driver超时时间
            #"automationName": "uiautomator2"

        }
        desired_caps["deviceName"] = self.device
        desired_caps.update()
        CreatAppiumDriver.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(self.url ,self.port), desired_caps)
        print CreatAppiumDriver.driver
        return CreatAppiumDriver.driver


    def kill_appium(self):
        '''
        结束appium进程
        :return:
        '''
        if os.popen('lsof -i:{}'.format(self.port)).read() == '':
            logger.info('appium pid is null')
        else:
            pid = os.popen('lsof -i:{}'.format(self.port)).readlines()[1].split()[1]
            os.system('kill -9 {}'.format(pid))
            logger.info('kill appium')


    def start_appium(self):
        '''
        启动appium服务
        :return:
        '''
        self.kill_appium()
        args = 'appium --log {} --session-override --udid {} -a  {} -p {}'.\
            format(self.appium_log,self.device ,self.url,self.port)
        logger.info('appium启动命令:{}'.format(args))
        appium = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, bufsize=1,close_fds=True)
        while True:
            appium_line = appium.stdout.readline().strip().decode()
            time.sleep(1)
            logger.info("启动appium中...")
            if 'Welcome to Appium' in appium_line or 'Error: listen' in appium_line:
                logger.info("appium启动成功")
                break



@pytest.fixture()
def appium_driver(scope="function"):
    device = '192.168.56.101:5555'
    pck_name = 'com.luojilab.player'
    lanuch_activity = 'com.luojilab.business.welcome.SplashActivity'
    logger.info("app测试开始!")
    create = CreatAppiumDriver(device, pck_name, lanuch_activity)
    create.start_appium()
    driver = create.init_capability()
    logger.info("启动app中.....")
    time.sleep(3)
    yield driver
    logger.info("app测试结束!")

class TestLogin():

    def test_login(self,appium_driver):
        '''
        登录测试
        :return:
        '''
        self.allow = "//*[@text='ALLOW']"
        self.allowtext = "//*[@text='允许']"
        self.minetab = "//*[@text='我的']"
        try:
            flag = True
            while flag:
                if Appium_Driver.find_elements(By.XPATH,self.allow):
                    Appium_Driver.find_element(By.XPATH,self.allow).click()
                    logger.info('点击授权')
                elif Appium_Driver.find_elements(By.XPATH,self.allowtext):
                    Appium_Driver.find_element(By.XPATH,self.allowtext).click()
                    logger.info('点击授权')
                else:
                    flag = False
                    break
            time.sleep(3)
        except Exception as e:
            logger.info('登录测试异常:{}'.format(e))



