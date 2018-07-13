# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
import sys
import os
import unittest
import random
import selenium.common.exceptions
from selenium import webdriver
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HTMLReport import logger


def findelementbyid(self, element):
    try:
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, element)))
        return True
    except selenium.common.exceptions.TimeoutException:
        return False
    except selenium.common.exceptions.NoSuchElementException:
        return False


def findelementbyxpath(self, element):
    try:
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, element)))
        return True
    except selenium.common.exceptions.TimeoutException:
        return False
    except selenium.common.exceptions.NoSuchElementException:
        return False


def swipeto(element):  # 翻页
    while True:
        try:
            #assertTrue(driver.find_element_by_xpath(element), '没找到')
            driver.find_element_by_xpath(element).click()
            break
        except:
            driver.swipe(200, 500, 200, 200, 500)
            sleep(2)
