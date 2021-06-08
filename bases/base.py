import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()


class Bases:

    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息，使用BY类
        :param timeout: 查找元素超时时间，默认30s
        :param poll: 查找元素的频率，默认0.5s
        :return:元素
        """
        log.info("正在调用查找元素方法，查找元素为：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素定位信息
        :param value: 输入的值
        """

        # 1. 获取元素
        el = self.base_find(loc)
        # 2. 清空
        log.info("正在清空：{}元素".format(loc))
        el.clear()
        # 3. 输入
        log.info("正在对：{} 元素进行输入操作，输入值为：{}".format(loc,value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        # 获取元素并点击
        log.info("正在执行点击:{} 元素的操作".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_test(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        log.info("正在执行获取:{} 元素的操作，获取文本为:{}".format(loc,self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 获取截图
        log.error("断言出错，正在获取错误截图")
        self.driver.get_screenshot_as_file("../image/err.png")
        # 写入报告
        log.error("断言出错，正在将错误截图写入allure报告")
        self.__base_writeing_img()

    # 将图片写入报告方法（私有化）
    def __base_writeing_img(self):
        # 获取文件流
        with open("../image/err.png", "rb") as f:
            # 调用allure.ayyach方法
            allure.attach("错误原因：", f.read(), allure.attachment_type.PNG)
