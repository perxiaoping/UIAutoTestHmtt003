from selenium.webdriver.common.by import By
from bases.base import Bases
from time import sleep


class WebBases(Bases):
    """以下方法为web专属"""

    # 下拉菜单选择方法封装
    def web_base_click_element(self, placeholder_text, click_text):
        # 1、点击父选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2、暂停
        sleep(1)
        # 3、点击文本
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 查找页面是否包含指定元素方法封装
    def web_bases_is_exist(self, text):
        # 组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 查找元素
        try:
            # 找元素 修改等待时间
            self.base_find(loc,timeout=3)
            # 找到了输出信息
            print("找到了 {} 元素".format(loc))
            return True
        except:
            # 未找到元素，输出信息
            print("未找到 {} 元素".format(loc))
            return False

