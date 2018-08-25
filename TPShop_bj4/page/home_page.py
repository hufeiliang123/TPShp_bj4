from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    mine_btn = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"
    login_sign_up_btn = By.XPATH, "//*[@text='登录/注册']"

    def click_mine(self):
        self.click(self.mine_btn)

    def click_login_sign_up(self):
        self.click(self.login_sign_up_btn)
