# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
from config import *


class Chat(unittest.TestCase):
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
        cls.driver = webdriver.Remote(remote, desired_caps)

    '''
    #  多个class执行的时候，会执行两次，暂时先去掉
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
'''
    def test_case1_进入患者聊天页(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
        el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
        el1.click()

        # TouchAction(self.driver).tap([(124,1259)],500)
        # TouchAction(self.driver).tap([(356, 999)], 500).perform()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/ib_add_patient")))
        el2 = self.driver.find_element_by_xpath("//*[@text='test']")
        el2.click()

    def test_case2_发送文本(self):
        # 发送文本
        el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_input")
        el3.click()
        el3.send_keys("hello")

        el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el4.click()
        sleep(3)
        #self.assertIsNotNone(self.self.driver.find_element_by_xpath("//*[@text='hello']"), '文本发送失败')

        el5 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_0")
        el5.click()

    def test_case3_发送语音(self):
        # 长按发送语音
        el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_press_speak")
        elx = el6.location.get('x')
        ely = el6.location.get('y')
        self.driver.swipe(elx, ely, elx, ely, 5000)
        sleep(3)
        self.assertIsNotNone(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_content"), '语音发送失败')

    def test_case4_发送图片(self):
        # 发送图片
        el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_1")
        el7.click()
        el8 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/chk_photo")
        el8.click()
        el9 = self.driver.find_element_by_xpath("//*[@text='发送(1)']")
        el9.click()

    def test_case5_发送表情(self):
        # 发送表情
        el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_4")
        el11.click()
        el12 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ViewSwitcher/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ViewSwitcher/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.GridView/android.widget.ImageView[1]")
        el12.click()
        el10.click()
