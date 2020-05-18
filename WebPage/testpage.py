# -*- encoding: utf-8 -*- 
from Include.commit.WebPage.basepage import BasePage
from Include.commit.WebPage.elementcrm import *
from Include.commit.Base.helper import Configparser
from selenium.webdriver.support.select import Select
import time,pytest
from functools import wraps
from selenium import webdriver

def input_bug(function):
    @wraps(function)
    def input(keys):
        for i in keys:
            function(i)
    return input


class TestBase():
    def setup_class(self):
        self.driver = Configparser().get_webdriver()

    def teardown_class(self):
        for windows in self.driver.window_handles:
            self.driver.switch_to.window(windows)
            self.driver.close()
        
    def setup_method(self):
        self.driver.get('http://admin.cstcrm.com/')
        login_page = login_page_loc(self.driver)
        login_page.input_username('admin')
        login_page.input_password('testsscf')
        login_page.click_submit()
        try:
            login_page.presence_of_element_located(By.CLASS_NAME, 'menu-text')
        except TimeoutException:
            print('登录失败')
    def teardown_method(self):
        mainpage = main_page(self.driver)
        if mainpage.is_login() == True:
            mainpage.click_user_info()
            mainpage.click_login_out()
    data = [('admin','testsscf')
        ,('admin1','fsdfgsdg')
            ]
    # @pytest.mark.parametrize('username,pwd',data)
    def test_login(self):
        mainpage = main_page(self.driver)
        fagroup_iframe = fa_group_iframe(self.driver)
        mainpage.click_fa_group()
        self.driver.find_elements_by_partial_link_text('业务员')[0].click()
        self.driver.switch_to.frame(1)#定位新开页面
        self.driver.find_elements_by_partial_link_text('模拟登陆')[0].click()


        self.driver.switch_to.window(self.driver.window_handles[1])
        mainpage.click_fa_comments()
        self.driver.find_elements_by_partial_link_text('全部客户')[0].click()
        self.driver.switch_to.frame(1)  # 定位新开页面
        fagroup_iframe.select_condition_field('手机号码')
        fagroup_iframe.input_keyword('')
        self.driver.find_element_by_class_name('search').click()
        self.driver.find_element_by_link_text('申请订单').click()
        self.driver.switch_to.parent_frame()
        
        self.driver.switch_to.frame(1)
        self.driver.switch_to.frame(0)
        self.driver.implicitly_wait(10)
        applyorder_main = apply_order(self.driver)
        applyorder_main.input_customer_name('jiukankan')
        applyorder_main.input_customer_qq()
        applyorder_main.input_customer_wechat()
        applyorder_main.select_customer_sex()
        self.driver.find_elements(*(By.NAME,'customer_sex'))[0].click()
        self.driver.find_element(*(By.NAME, 'customer_age')).send_keys('customer_age')
        self.driver.find_element(*(By.NAME, 'customer_fund_amount')).send_keys('customer_fund_amount')
        self.driver.find_element(*(By.NAME, 'id_card')).send_keys('id_card')
        self.driver.find_element(*(By.NAME, 'customer_address')).send_keys('customer_address')
        self.driver.find_element(*(By.NAME, 'salesman_name')).send_keys('salesman_name')
        Select(
            self.driver.find_element(*(By.NAME, 'package_id'))
        ).select_by_visible_text('春雨操盘')
        self.driver.find_element(*(By.NAME, 'order_fee')).send_keys('order_fee')
        self.driver.find_elements(*(By.NAME,'is_promptly_dredge'))[1].click()
        self.driver.find_element(*(By.NAME, 'start_serve_time')).send_keys('2020-05-07')
        self.driver.find_element(*(By.NAME, 'end_serve_time')).send_keys('2020-05-08')
        Select(
            self.driver.find_element(*(By.NAME,'receipt_bank_record'))
        ).select_by_visible_text('现金-')
        self.driver.find_element(*(By.NAME, 'account_perform_time')).send_keys('2020-05-06 17:12')
        self.driver.find_element(*(By.NAME,"performance_fee")).send_keys('100')
        
        self.driver.find_elements(*(By.NAME, 'is_phoenix_resource'))[1].click()
        self.driver.find_elements(*(By.CLASS_NAME, 'pay_reason'))[1].click()
        time.sleep(5)
        self.driver.find_elements(*(By.CLASS_NAME, 'customer_nature'))[1].click()
        self.driver.find_elements(*(By.CLASS_NAME, 'talk_plan'))[1].click()
        self.driver.find_element(*(By.NAME,'other_talk_plan')).send_keys('other_talk_plan')
        self.driver.find_elements(*(By.NAME, 'customer_profession'))[1].click()
        self.driver.find_elements(*(By.CLASS_NAME, 'other_explain'))[0].click()
        self.driver.find_elements(*(By.NAME, 'profession'))[0].click()
        self.driver.find_elements(*(By.NAME, 'into_stock_time'))[0].click()
        self.driver.find_elements(*(By.NAME, 'into_stock_profit'))[0].click()
        self.driver.find_elements(*(By.NAME, 'investment_style'))[0].click()
        self.driver.find_elements(*(By.NAME, 'is_guide'))[0].click()
        self.driver.find_elements(*(By.NAME, 'serve_model'))[0].click()
        self.driver.find_elements(*(By.NAME, 'operator_style'))[0].click()
        self.driver.find_elements(*(By.NAME, 'investment_strategy'))[0].click()
        self.driver.find_elements(*(By.NAME, 'serve_plan'))[0].click()
        time.sleep(20)