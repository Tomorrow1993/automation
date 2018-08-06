# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
from config import *


class Login(unittest.TestCase):
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
	def test_register_判断是否有欢迎页面后点击注册(self):  # 判断是否有欢迎页，然后注册
		if findelementbyid(self, 'com.kanchufang.privatedoctor:id/lrchoose_register_btn'):
			self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_register_btn").click()
			self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/register_hint_dialog_start_btn").click()
		else:
			self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_register_tv").click()
			self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/register_hint_dialog_start_btn").click()

	def create_phone_随机生成手机号(self):  # 随机生成手机号
		li = '0123456789'
		top = '210'
		self.phone = top + "".join(random.choice(li) for i in range(8))
		self.password = 'qqqqqq'
		self.name = 'test'

	def test_case1_注册(self):  # 注册
		self.create_phone()
		el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_phone")
		el1.click()
		el1.send_keys(self.phone)

		el2 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_password")
		el2.click()
		el2.send_keys(self.password)

		el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_confirm_password")
		el3.click()
		el3.send_keys(self.password)

		el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_validation_captcha")
		el4.click()
		el4.send_keys("aaaa")

		el5 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_next")
		el5.click()
		'''
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/warn_dialog_yes_btn").click()

		el4.send_keys("1111")
		el5.click()

		#调用注册API
		payload = {'phone':phone,'password':password}
		r = requests.post('https://yisheng.aihaisi.com/api/register/test',data = payload)
		
		'''
	def test_case2_填写个人信息(self):  # 填写个人信息
		self.create_phone_随机生成手机号()
		WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_start_trust_doctor")))
		name = 'test'
		#sleep(9)
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_name")
		el6.click()
		el6.send_keys(self.name)

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_hosptial").click()
		sleep(3)
		self.driver.find_element_by_xpath("//*[@text='上海']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='上海市']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='黄浦区']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='上海长征医院']").click()

		self.assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_select_hosptial").text,"上海长征医院","执业点pass")
		
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='泌尿外科/男科']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='男科']").click()
		#assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"男科","科室lose")

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_position").click()
		self.driver.find_element_by_xpath("//*[@text='主任医师']").click()
		#assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"主任医师","职称lose")

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_start_trust_doctor").click()
		#assertIsNone(self.driver.find_element_by_id('com.kanchufang.privatedoctor:id/tab_home_rb'),"登录失败")

	def	test_case3_切换至我tab退出登陆(self):  # 切换到我tab，退出登录
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_me_rb")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/menu_setting").click()
		sleep(2)
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_modify_password")
		el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_flow_mode")
		self.driver.scroll(el7, el6)

		#self.driver.swipe(500,1500,500,500,1000)
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_logout").click()
		sleep(1)
		self.driver.find_element_by_id("android:id/button1").click()
		sleep(5)

	def test_login_再次判断是否有欢迎页(self):  # 判断是否有欢迎页，然后登录
			if findelementbyid(self, 'com.kanchufang.privatedoctor:id/lrchoose_login_btn'):
				self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_login_btn").click()
			else:
				pass

	def test_case4_登陆(self):  # 登录
		el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/password_et")
		el10.click()
		el10.send_keys('qqqqqq')
		'''
		if el8.is_displayed():
			el8.click()
			el9.click()
			el9.send_keys(phone)
		else:
			el10.click()
			el9.click()
			el9.send_keys(phone)
		el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/password_et")
		el10.click()
		el10.send_keys(password)
		'''
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_btn").click()
		#WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		#assertIsNotNone(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_home_rb"),'登录失败')

	def test_case5_认证(self):  # 认证
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_edit_profile").click()
		
		el11 = self.driver.find_element_by_xpath("//*[@text='医生认证']")
		el11.click()
		el12 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload")
		el12.click()
		el13 = self.driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		sleep(1)
		el14 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.CheckBox")
		el15 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.CheckBox")
		el14.click()
		el16 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/select")
		el16.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload").click()
		self.driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_auth_verify")))
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='您的认证正在审核中…']"),'普通认证提交失败')
		el17 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_auth_verify")
		el17.click()
		
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_upload")))
		el12.click()
		el13 = self.driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		el14.click()
		el15.click()
		el16.click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		el12.click()
		self.driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID,"android:id/message")))
		#assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='上传成功，请耐心等待审核。']"),'权威认证提交失败')

