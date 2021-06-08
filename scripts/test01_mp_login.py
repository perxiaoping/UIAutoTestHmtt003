import pytest
from tools.get_driver import GetDriver
from page.page_in import PageIn
import page
from time import sleep

from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.web_url)
        # 2.通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        # sleep(3)
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test_mp_login(self, username="", code="macro123", expect="后台项目!!"):
        # 调用登录业务方法
        self.mp.page_mp_login(username, code)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误内容为：{}".format(e))
            print("异常信息为：", e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise
