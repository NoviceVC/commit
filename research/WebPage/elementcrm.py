# -*- encoding: utf-8 -*-
from Include.research.WebPage.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver





class login_page_loc(BasePage):
    _username_loc = (By.ID, 'js-admin-name')
    _password_loc = (By.ID, 'admin_pwd')
    _submit_loc = (By.NAME, 'submit')

    @BasePage.is_ele_TimeoutException
    def input_username(self, keys):
        element = self.presence_of_element_located(*self._username_loc)
        element.clear()
        return element.send_keys(keys)

    @BasePage.is_ele_TimeoutException
    def input_password(self, keys):
        return self.presence_of_element_located(*self._password_loc).send_keys(keys)

    @BasePage.is_ele_TimeoutException
    def click_submit(self):
        return self.presence_of_element_located(*self._submit_loc).click()

class main_page(BasePage):
    _user_info_loc = (By.CLASS_NAME, 'user-info')
    _login_out_loc = (By.LINK_TEXT, '退出')
    _menu_text_locs = (By.CLASS_NAME, 'menu-text')
    _fa_group_loc = (By.CLASS_NAME, 'fa-group')  # 注意菜单栏是通过图标定位的，可能存在相同图标
    _fa_comments_loc = (By.CLASS_NAME, 'fa-comments')
    @BasePage.is_ele_TimeoutException
    def click_user_info(self):
        # 用户信息
        return self.presence_of_element_located(*self._user_info_loc).click()

    @BasePage.is_ele_TimeoutException
    def click_login_out(self):
        # 退出
        return self.presence_of_element_located(*self._login_out_loc).click()

    def is_login(self):
        # 是否存在菜单栏
        return self.is_element_exist(*self._menu_text_locs)

    @BasePage.is_ele_TimeoutException
    def click_fa_group(self):
        # 定位用户管理菜单栏
        fa_group = self.presence_of_all_elements_located(*self._fa_group_loc)
        return fa_group[0].click()
    
    def click_fa_comments(self):
        # 定位用户管理菜单栏
        fa_group = self.presence_of_all_elements_located(*self._fa_comments_loc)
        return fa_group[0].click()
class fa_group_iframe(BasePage):
    _keyword_loc = (By.NAME,'keyword')
    def input_keyword(self,keys):
        return self.presence_of_element_located(*self._keyword_loc).send_keys(keys)
