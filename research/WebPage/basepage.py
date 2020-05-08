# -*- encoding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
from functools import wraps


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    
    def is_ele_TimeoutException(function):
        # 调用错误报告，页面不存在时返回
        @wraps(function)
        def fuc(*args, **kwarg):
            try:
                function(*args, **kwarg)
            except TimeoutException:
                func_name = function.__name__
                print('不存在%s的loc' % (func_name))
        return fuc
    def is_element_exist(self,*loc):
        # 页面是否存在该element
        flag = self.driver.find_elements(*loc)
        if len(flag) == 0:
            # print("元素未找到:%s" % loc[1])
            return False
        elif len(flag) > 1:
            return True
            # print("找到%s个元素：%s" % (len(flag), loc[1]))
    # def must_find(self,*locator,a=1):
    #     if a1:
    #         return WebDriverWait(self.driver, 5, 0.2).until(
    #             EC.presence_of_all_elements_located(locator)
    #         )
    #     elif a ==None:
    #         return WebDriverWait(self.driver, 5, 0.2).until(
    #             EC.presence_of_elements_located(locator)
    #         )


    def presence_of_all_elements_located(self,*locator):

        return WebDriverWait(self.driver, 5, 0.2).until(
            EC.presence_of_all_elements_located(locator)
        )

    def presence_of_element_located(self,*locator):
        return WebDriverWait(self.driver, 5, 0.2).until(
            EC.presence_of_element_located(locator)
        )
