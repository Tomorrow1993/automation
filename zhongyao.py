# -*- coding: utf-8 -*-
# @created on 2018/6/14 上午11:19
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
from config import *


class Zhongyao(unittest.TestCase):
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

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_case1_进入中药首页(self):  # 进入中药首页
		WebDriverWait(self.driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
		el1.click()
		el2 = self.driver.find_element_by_xpath("//*[@text='test']")
		el2.click()
		el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_3")
		el3.click()

	def test_case2_设置诊费_诊断(self):  # 设置诊费、诊断
		el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_medicine_consult_fee_value")
		el4.click()
		el5 = self.driver.find_element_by_xpath("//*[@text='免费']")
		el5.click()
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_et_input")
		el6.send_keys("感冒")

	def test_case3_设置剂型(self):  # 设置剂型
		el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_medicine_type_value")
		el7.click()
		el8 = self.driver.find_element_by_xpath("//*[@text='膏方']")
		el8.click()

	def test_case4_添加药材_常用方(self):  # 添加药材、添加常用方
		swipeto("//*[@text='添加药材']")
		el9 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_tv_mine")
		el9.click()
		el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_tv_add_template0")
		el10.click()
		el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_et_input")
		el11.send_keys('test')
		el12 = self.driver.find_element_by_id("android:id/button1")
		el12.click()

		el13 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_et_search")
		el13.send_keys('cpp')
		if findelementbyxpath(self, "//*[@text='未搜索到此药材，建议使用其他药材代替']"):  # 以防没有找到'cpp'开头的药
			el13.clear()
			el13.send_keys('chj')
		else:
			pass
		el14 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ViewSwitcher/android.support.v7.widget.RecyclerView/android.widget.TextView")
		el14.click()
		el15 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_tv_num")
		el15.clear()
		el15.send_keys('1000')
		el16 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_menu_save")
		el16.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='test']")))
		el17 = self.driver.find_element_by_xpath("//*[@text='test']")
		el17.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/zy_iv_del")))
		el16.click()

	def test_case5_添加辅料(self):  # 添加辅料
		swipeto("//*[@text='添加辅料']")
		if findelementbyxpath(self, "//*[@text='添加辅料']"):
			self.driver.find_element_by_xpath("//*[@text='添加辅料']").click()
		else:
			pass
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tv_tag")))
		el13 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View/android.widget.TextView[1]")
		el13.click()
		el14 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_tv_num")
		el14.clear()
		el14.send_keys('1000')
		el15 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_menu_save")
		el15.click()

	def test_case6_推荐中药(self):  # 推荐中药
		el16 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/zy_tv_recommend")
		el16.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/btn_send")))
		if findelementbyid(self, "com.kanchufang.privatedoctor:id/layout_content"):
			logger().info("聊天页存在中药推荐记录")
		else:
			logger().info("聊天页不存在中药推荐记录")




