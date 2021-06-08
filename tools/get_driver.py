from selenium import webdriver


class GetDriver:
    # 声明变量
    __web_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取driver
            cls.__web_driver = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/chromedriver")
            # 最大化
            cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 退出driver
    @classmethod
    def quit_web_driver(cls):
        # 判断是否为空
        if cls.__web_driver:
            # 不为空退出
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None



# GetDriver()
# GetDriver.get_web_driver("http://www.baidu.com")
# GetDriver.quit_web_driver()