# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
from config import *


class Payment(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '8.1.0'  # 6.0 4.4.2
		desired_caps['deviceName'] = 'db172033'  # 1bf493ad c66d2f78 emulator-555444
		desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
		desired_caps['appActivity'] = '.activities.start.SplashActivity'
		desired_caps['noReset'] = 'true'
		desired_caps['clearSystemFiles'] = 'true'
		desired_caps['unicodeKeyboard'] = 'true'
		# desired_caps['automationName'] = 'uiautomator2' # 支持android7.0版本+
		cls.driver = webdriver.Remote(remote, desired_caps)

	''' 
	#  多个class执行的时候，会执行两次，暂时先去掉
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
'''
	def test_case1_开通收费(self):  # 开通收费
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_work_site_rb")
		el1.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='线下工作室']")))

		el2 = self.driver.find_element_by_xpath("//*[@text='杏仁门诊']")
		el3 = self.driver.find_element_by_xpath("//*[@text='新的执业地点']")
		self.driver.scroll(el3, el2)

		sleep(3)
		el4 = self.driver.find_element_by_xpath("//*[@text='包月咨询']")
		el4.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='99元/月']")))
		el5 = self.driver.find_element_by_xpath("//*[@text='99元/月']")
		el5.click()
		
		sleep(3)
		el6 = self.driver.find_element_by_xpath("//*[@text='图文咨询']")
		el6.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='19元/次']")))
		el7 = self.driver.find_element_by_xpath("//*[@text='19元/次']")
		el7.click()

		sleep(3)
		el8 = self.driver.find_element_by_xpath("//*[@text='电话咨询']")
		el8.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='49元/次']")))
		el9 = self.driver.find_element_by_xpath("//*[@text='49元/次']")
		el9.click()

	'''
	def test_case2_调API添加患者(self):#调API添加患者
		test
	'''

	def test_case3_图文咨询(self):#图文咨询
		#购买图文API
		#调用购买图文付费的API
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb").click()
		#assertIsNotNone(self.driver.find_element_by_id("id/tab_patient"),'没有找到这个ID')
		if findelementbyxpath(self, "//*[@text='VIP']"):
			pass
		else:
			logger().info('消息列表无图文VIP')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无图文VIP')
		el10 = self.driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tv_sort_by_fee")))
		if findelementbyxpath(self, "//*[@text='test']"):
			pass
		else:
			logger().info('VIP患者分组内无患者')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		if findelementbyxpath(self, "//*[@text='VIP付费：图文咨询  |  1']"):
			pass
		else:
			logger().info('图文咨询分组内无患者')
		'''
		el12 = self.driver.find_element_by_xpath("//*[@text='VIP付费：图文咨询]")
		el12.click()
		'''
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'图文咨询分组内无患者')
		self.driver.press_keycode('4')
		sleep(1)
		self.driver.press_keycode('4')
		sleep(1)

		el13 = self.driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_send")))
		if findelementbyxpath(self, "//*[@text='VIP图文']"):
			pass
		else:
			logger().info('聊天页患者名字下面没有VIP图文')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='VIP图文']"),'聊天页患者名字下面没有VIP图文')
		self.driver.swipe(1000, 800, 100, 800)
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='咨询订单']")))
		self.assertIn('图文咨询', self.driver.page_source,'服务套餐tab图文状态未更新')
		self.driver.press_keycode('4')

		#退款图文API

	def test_case4_包月咨询(self):#包月咨询
		# 购买包月API
		# 调用购买包月付费的API
		if findelementbyxpath(self, "//*[@text='咨询订单']"):
			self.driver.press_keycode('4')
		else:
			pass
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb").click()
		# assertIsNotNone(self.driver.find_element_by_id("id/tab_patient"),'没有找到这个ID')
		if findelementbyxpath(self, "//*[@text='VIP']"):
			pass
		else:
			logger().info('消息列表无包月VIP')
		# assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无图文VIP')
		el10 = self.driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tv_sort_by_fee")))
		if findelementbyxpath(self, "//*[@text='test']"):
			pass
		else:
			logger().info('VIP患者分组内无患者')
		# assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		if findelementbyxpath(self, "//*[@text='VIP付费：包月咨询  |  1']"):
			pass
		else:
			logger().info('包月咨询分组内无患者')

		# assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'图文咨询分组内无患者')
		self.driver.press_keycode('4')
		sleep(1)
		self.driver.press_keycode('4')
		sleep(1)

		el13 = self.driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/btn_send")))
		if findelementbyxpath(self, "//*[@text='VIP包月']"):
			pass
		else:
			logger().info('聊天页患者名字下面没有VIP包月')
		# assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='VIP图文']"),'聊天页患者名字下面没有VIP图文')
		self.driver.swipe(1000, 800, 100, 800)
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='咨询订单']")))
		self.assertIn('包月咨询', self.driver.page_source, '服务套餐tab包月状态未更新')
		self.driver.press_keycode('4')

	def test_case5_电话咨询(self):#电话咨询
		#购买电话# API
		if findelementbyxpath(self, "//*[@text='咨询订单']"):
			self.driver.press_keycode('4')
		else:
			pass

		if findelementbyxpath(self, "//*[@text='VIP']"):
			pass
		else:
			logger().info('消息列表无电话VIP')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无电话VIP')
		el10 = self.driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		if  findelementbyxpath(self, "//*[@text='test']"):
			pass
		else:
			logger().info('VIP患者分组内无患者')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		sleep(1)
		if findelementbyxpath(self, "//*[@text='VIP付费：电话咨询  |  1']"):
			pass
		else:
			logger().info('电话咨询分组内无患者')
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='test']"),'电话咨询分组内无患者')
		self.driver.press_keycode('4')
		sleep(1)
		self.driver.press_keycode('4')
		sleep(1)
		el13 = self.driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		if findelementbyid(self, "com.kanchufang.privatedoctor:id/iv_goto_call"):
			pass
		else:
			logger().info('聊天页没有电话弹窗')
		#assertIsNotNone(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/iv_goto_call",'聊天页没有电话弹窗'))
