from bases.base import Bases
import page
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageMisLogin(Bases):
    # 1.输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 2.输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 3.点击登录
    def page_click_login_btn(self):
        # 1.处理js（项目特殊）
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        # 2.点击登录方法
        self.base_click(page.mis_login_btn)

    # 4.获取昵称文本
    def page_get_nickname(self):
        return self.base_get_test(page.mis_nickname)

    # 5.组合后台管理系统登录方法
    def page_mis_login(self, username, pwd):
        log.info("正在调用组合后台登录方法，用户名：{} ,密码：{}".format(username,pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 6.组合后台管理系统登录方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用组合后台登录成功依赖方法，用户名：{} ,密码：{}".format(username,pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()