# -*- coding: utf-8 -*-
# @created on 2018/6/12 上午10:31
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'  # 6.0 4.4.2
desired_caps['deviceName'] = '1bf493ad'  # 1bf493ad c66d2f78 emulator-555444
desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
desired_caps['appActivity'] = '.activities.start.SplashActivity'
desired_caps['noReset'] = 'true'
desired_caps['clearSystemFiles'] = 'true'
desired_caps['unicodeKeyboard'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)