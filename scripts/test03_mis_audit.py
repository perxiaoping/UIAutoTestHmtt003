from page.page_in import PageIn
from tools.get_driver import GetDriver
import page


class TestMisAudit:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.mis_url)
        # 2、获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3、调用成功登录依赖方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4、通过统一入口类对象获取PageMisAudit
        self.audit = PageIn(driver).page_get_PageMisAudit()

    # 2、结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、调用文章审核方法
    def test_mis_audit(self, title="虎虎虎虎虎虎", channel="开发者资讯"):
        # 1、调用后台文章审核方法
        self.audit.page_mis_audit(title,channel)
        # 2、断言
        self.audit.page_assert_audit()
