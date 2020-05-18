# -*- encoding: utf-8 -*-
from Include.commit.WebPage.basepage import BasePage
from selenium.webdriver.common.by import By

class login_page_loc(BasePage):
    """
    登录页面ele
    """
    _username_loc = (By.ID, 'js-adminname')
    _password_loc = (By.ID, 'admin_pwd')
    _submit_loc = (By.NAME, 'submit')
    def input_username(self, username):
        return self.must_input(username,*self._username_loc)

    def input_password(self, password):
        return self.must_input(password,*self._password_loc)

    def click_submit(self):
        return self.presence_of_element_located(*self._submit_loc).click()

class main_page(BasePage):
    """
    主菜单页面ele
    """
    _user_info_loc = (By.CLASS_NAME, 'user-info')
    _login_out_loc = (By.LINK_TEXT, '退出')
    _menu_text_locs = (By.CLASS_NAME, 'menu-text')
    _fa_group_loc = (By.CLASS_NAME, 'fa-group')  # 注意菜单栏是通过图标定位的，可能存在相同图标
    _fa_comments_loc = (By.CLASS_NAME, 'fa-comments')
    def click_user_info(self):
        # 用户信息
        return self.presence_of_element_located(*self._user_info_loc).click()

    def click_login_out(self):
        # 退出
        return self.presence_of_element_located(*self._login_out_loc).click()

    def is_login(self):
        # 是否存在菜单栏
        return self.is_element_exist(*self._menu_text_locs)

    def click_fa_group(self):
        # 定位用户管理菜单栏
        fa_group = self.presence_of_all_elements_located(*self._fa_group_loc)
        return fa_group[0].click()
    
    def click_fa_comments(self):
        # 定位用户管理菜单栏
        fa_group = self.presence_of_all_elements_located(*self._fa_comments_loc)
        return fa_group[0].click()
class fa_group_iframe(BasePage):
    """
    第一iframe页面
    """
    _condition_field_loc = (By.NAME,'condition-field')
    _keyword_loc = (By.NAME,'condition-content-input')
    def input_keyword(self,keys):
        return self.must_input(keys,*self._keyword_loc)
    def select_condition_field(self,visible_text):
        return self.must_select(visible_text,*self._condition_field_loc)
class apply_order(BasePage):
    """
    业务员提单页面ele
    """
    _customer_name_loc = (By.NAME,'customer_name')
    _customer_qq_loc = (By.NAME,'customer_qq')
    _customer_wechat_loc = (By.NAME,'customer_wechat')
    _customer_sex_loc = (By.NAME,'customer_sex')
    _customer_age_loc = (By.NAME, 'customer_age')
    _customer_fund_amount_loc = (By.NAME, 'customer_fund_amount')
    _id_card_loc = (By.NAME, 'id_card')
    _customer_address_loc = (By.NAME, 'customer_address')
    _salesman_name_loc = (By.NAME, 'salesman_name')
    _package_id_loc = (By.NAME, 'package_id')
    _order_fee_loc = (By.NAME, 'order_fee')
    _is_promptly_dredge_loc = (By.NAME,'is_promptly_dredge')
    _start_serve_time_loc = (By.NAME, 'start_serve_time')
    _end_serve_time_loc = (By.NAME, 'end_serve_time')
    _receipt_bank_record_loc = (By.NAME,'receipt_bank_record')
    _account_perform_time_loc = (By.NAME, 'account_perform_time')
    _performance_fee_loc = (By.NAME,"performance_fee")
    _is_phoenix_resource_loc = (By.NAME, 'is_phoenix_resource')
    _pay_reason_loc = (By.CLASS_NAME, 'pay_reason')
    _customer_nature_loc = (By.CLASS_NAME, 'customer_nature')
    _talk_plan_loc = (By.CLASS_NAME, 'talk_plan')
    _other_talk_plan_loc = (By.NAME,'other_talk_plan')
    _customer_profession_loc = (By.NAME, 'customer_profession')
    _other_explain_loc = (By.CLASS_NAME, 'other_explain')
    _profession_loc = (By.NAME, 'profession')
    _into_stock_time_loc = (By.NAME, 'into_stock_time')
    _into_stock_profit_loc = (By.NAME, 'into_stock_profit')
    _investment_style_loc = (By.NAME, 'investment_style')
    _is_guide = (By.NAME, 'is_guide')
    _serve_model_loc = (By.NAME, 'serve_model')
    _operator_style_loc = (By.NAME, 'operator_style')
    _investment_strategy_loc = (By.NAME, 'investment_strategy')
    _serve_plan_loc = (By.NAME, 'serve_plan')
    def input_customer_name(self,customer_name):
        return self.must_input(customer_name,*self._customer_name_loc)
    def input_customer_qq(self,customer_qq):
        return self.must_input(customer_qq,*self._customer_qq_loc)
    def input_customer_wechat(self,customer_wechat):
        return self.must_input(customer_wechat,*self._customer_wechat_loc)
    def select_customer_sex(self,visible_text):
        return Select(
            self.input_customer_name(self._customer_sex_loc)
        ).select_by_visible_text(visible_text)
