# -*- coding: utf-8 -*-
# @created on 2018/5/7 上午11:18
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路
from config import *


class AddTaoc(unittest.TestCase):

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
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
        el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
        el1.click()
        el2 = self.driver.find_element_by_xpath("//*[@text='test']")
        el2.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/cib_2")))
        el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_2")
        el3.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_recommend")))
        el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_fl_drug_set")
        el4.click()
        if findelementbyid(self, "com.kanchufang.privatedoctor:id/yf_tv_add_template"):
            self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_add_template").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='添加用药套餐']").click()

    def test_case2_搜索药品(self):  # 搜索药品
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_et_template_input")))
        el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_et_template_input")
        el6.send_keys("test")
        self.driver.hide_keyboard()
        el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_add_now")
        el7.click()
        sleep(2)
        el8 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_act_search")
        el8.send_keys('感冒灵')
        # 切换回第三方键盘，只有三方键盘才能点键盘上的回车键
        sleep(2)
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        # 点击键盘上回车键
        sleep(2)
        self.driver.press_keycode(66)
        sleep(2)
        el9 = self.driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='药品'])[1]")
        el9.click()

    def test_case3_加入用药套餐(self):  # 加入用药套餐
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_btn_add_recommend")))
        el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_btn_add_recommend")
        el10.click()
        self.driver.press_keycode('4')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_any_elements_located((By.ID, "com.kanchufang.privatedoctor:id/menu_save")))
        el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/menu_save")
        el11.click()

    def test_case4_加入推荐单(self):  # 加入推荐单
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_tv_save_to_set")))
        el12 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_save_to_set")
        el12.click()