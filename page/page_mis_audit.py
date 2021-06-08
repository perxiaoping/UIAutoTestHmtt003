from bases.base import Bases
from time import sleep
import page
from bases.web_bases import WebBases


class PageMisAudit(WebBases):
    # 文章ID
    article_id = None

    # 1、信息管理
    def page_click_info_manage(self):
        # 暂停时间
        sleep(1)
        self.base_click(page.mis_info_manage)

    # 2、内容审核
    def page_click_content_audit(self):
        # 暂停时间
        sleep(1)
        self.base_click(page.mis_content_audit)

    # 3、文章标题
    def input_title(self, title):
        self.base_input(page.mis_title, title)

    # 4、输入频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 5、选择状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    # 6、点击查询
    def page_click_find(self):
        self.base_click(page.mis_find)

    # 7、获取ID
    def get_article_id(self):
        # 暂停时间
        sleep(1)
        return self.base_get_test(page.mis_article_id)

    # 8、点击通过
    def page_click_pass_btn(self):
        # 暂停时间
        sleep(1)
        self.base_click(page.mis_pass_btn)

    # 9、点击确认
    def page_click_confirm_pass(self):
        # 暂停时间
        sleep(1)
        self.base_click(page.mis_confirm_pass_btn)

    # 10、组合发布文章的业务方法
    def page_mis_audit(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.get_article_id()
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 11.组装断言业务操作方法
    def page_assert_audit(self):
        # 1.暂停3秒
        sleep(3)
        # 2.修改状态-》审核通过
        self.web_base_click_element(placeholder_text="请选择状态",click_text="审核通过")
        # 3.点击查询按钮
        self.page_click_find()
        # 4.判断当前页面是否存在指定元素并返回结果
        return self.web_bases_is_exist(self.article_id)