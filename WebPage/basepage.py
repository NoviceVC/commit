# -*- encoding: utf-8 -*-
import inspect,os,time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
from functools import wraps
from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def is_ele_TimeoutException(function):
        # 调用错误报告，页面不存在ele时返回
        @wraps(function)
        def fuc(*args, **kwarg):
            try:
                function(*args, **kwarg)
            except TimeoutException:
                func_name = function.__name__
                print('不存在%s的loc' % (func_name
                ))
        return fuc


    def presence_of_all_elements_located(self,*locator,run_time=5,diff_time=0.2):
        try :
            return WebDriverWait(self.driver, run_time, diff_time).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            print('%s存在错误'%(inspect.stack()[3][0]))
            return False


    def presence_of_element_located(self,*locator,run_time=5,diff_time=0.2):
        try:
            return WebDriverWait(self.driver, run_time, diff_time).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print('%s存在错误'%(inspect.stack()[3][0]))
            return False

    def must_input(self,keys,*locator):
        is_loc = self.presence_of_element_located(*locator)
        if is_loc != False:
            self.driver.find_element(*locator).clear()
            for i in keys:
                self.driver.find_element(*locator).send_keys(i)
        else:
            # 不存在ele时不进行操作
            pass

    def must_select(self,visible_text,*locator):
        is_loc = self.presence_of_element_located(*locator)
        if is_loc != False:
            Select(
                self.driver.find_element(*locator)
            ).select_by_visible_text(visible_text)
        else:
            pass

    def must_radio(self):
        is_loc = self.presence_of_all_elements_located(*locator)
        if is_loc != False:
            Select(
                self.driver.find_element(*locator)
            ).select_by_visible_text(visible_text)
        else:
            pass



    def must_checkbox(self):
        is_loc = self.presence_of_all_elements_located(*locator)
        if is_loc != False:
            Select(
                self.driver.find_element(*locator)
            ).select_by_visible_text(visible_text)
        else:
            pass
