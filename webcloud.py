# -*- encoding:utf-8 -*-
from selenium import webdriver
import unittest, time, csv
from testcase import login, update_pwd
#添加备注
# 登陆测试类
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://121.41.108.245:9191/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 登录case
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        with open("C:\\Python34\\example\\testdata\\userinfo.csv") as csvfile:
            userinfo = csv.reader(csvfile)
            for row in userinfo:
                # 登录
                login.login(self, row[0], row[1])
                # 我的账户
                driver.find_element_by_xpath("//a[@href='/account']").click()
                time.sleep(2)
                # 退出
                login.logout(self)

    # 修改密码case
    def test_updatepwd(self):
        driver = self.driver
        driver.get(self.base_url)
        # 登录
        login.login(self, "13564150520", "123qwe")
        # 进入用户资料页面修改密码
        driver.find_element_by_xpath("//a[@href='/account']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@href='/account/userinfo']").click()
        with open("C:\\Python34\\example\\testdata\\pwd.csv") as csvfile:
            pwdinfo = csv.reader(csvfile)
            for row in pwdinfo:
                update_pwd.updatepwd(self, row[0], row[1], row[2])
        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#执行用例
if __name__ == "__main__":
    unittest.main()

