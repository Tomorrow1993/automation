# -*- coding: utf-8 -*-
# @created on 2018/5/11 上午11:49
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路
from config import *


class CollectDrugs(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '8.1.0'  # 6.0 4.4.2
		desired_caps['deviceName'] = '1bf493ad'  # 1bf493ad c66d2f78 emulator-555444
		desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
		desired_caps['appActivity'] = '.activities.start.SplashActivity'
		desired_caps['noReset'] = 'true'
		desired_caps['clearSystemFiles'] = 'true'
		desired_caps['unicodeKeyboard'] = 'true'
		desired_caps['automationName'] = 'uiautomator2' # 支持android7.0版本+
		# desired_caps['resetKeyboard'] = 'true'
		cls.driver = webdriver.Remote(remote, desired_caps)

	''' 
	#  多个class执行的时候，会执行两次，暂时先去掉
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
'''
	def test_case1_进入西药首页(self):  # 进入西药首页
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
		el1.click()
		el2 = self.driver.find_element_by_xpath("//*[@text='test']")
		el2.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/cib_2")))
		el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_2")
		el3.click()

	def test_case2_点击一项药品进行收藏(self):  # 点击一项药品进行收藏
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_recommend")))
		el4 = self.driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='药品'])[1]")
		el4.click()
		el5 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_ll_collect")
		el5.click()

	def test_case3_去我的收藏页校验(self):  # 去我的收藏页校验
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_iv_close")
		el6.click()
		el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_fl_my_collect")
		el7.click()
		sleep(2)
		if findelementbyid(self, "com.kanchufang.privatedoctor:id/yf_tv_empty"):
			logger().info("我的收藏内无记录")
		else:
			logger().info("收藏成功")
