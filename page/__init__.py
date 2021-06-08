from selenium.webdriver.common.by import By

"""以下数据为url数据"""
web_url = "http://www.macrozheng.com/admin/#/login"
mis_url = "http://ttmis.research.itcast.cn/#/"


"""以下数据为自媒体模块配置数据"""
# 用户名
mp_username = By.CSS_SELECTOR, "[placeholder='请输入用户名']"
# 验证码
mp_code = By.CSS_SELECTOR, "[placeholder='请输入密码']"
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div[1]/div/div[1]"


"""以下数据为后台登录配置数据"""
# 用户名
mis_username = By.CSS_SELECTOR, "[name='username']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[name='password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取昵称
mis_nickname = By.CSS_SELECTOR, ".user_info"
# 信息管理
mis_info_manage = By.XPATH, "//*[text()='信息管理']/."
# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']/."
# 输入文章标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 输入频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询
mis_find = By.CSS_SELECTOR, ".find"
# 获取id
mis_article_id = By.CSS_SELECTOR, ".cell>span"
# 通过按钮
mis_pass_btn = By.XPATH, "//*[text()='通过']/.."
# 确认按钮
mis_confirm_pass_btn = By.CSS_SELECTOR, ".el-button--primary"
