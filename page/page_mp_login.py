from bases.base import Bases
import page
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()

class PageMpLogin(Bases):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称封装
    def page_get_nickname(self):
        return self.base_get_test(page.mp_nickname)

    # 组合业务方法
    def page_mp_login(self, username, code):
        log.info("正在执行自媒体登录操作，用户名：{}，密码：{} ".format(username,code))
        self.page_input_username(username)
        self.page_input_code(code)
        sleep(1)
        self.page_click_login_btn()
