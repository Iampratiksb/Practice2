import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import Loggen


class Test_001_Login:
    baseURL = readConfig.getApplicationURL()
    username = readConfig.getUseremail()
    password = readConfig.getPassword()

    logger = Loggen.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("**************************** test_HomePageTitle initializing ********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("*************************** test_HomePageTitle Test Case Passed ********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_HomePageTitle.png")
            self.logger.error("*************************** test_HomePageTitle Test Case Failed ********************************")
            self.driver.close()
            assert False


    def test_Login(self, setup):
        self.logger.info("**************************** test_Login initializing ********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************************** test_Login Test Case Passed ********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_Login.png")
            self.logger.error("**************************** test_Login Test Case Failed ********************************")
            self.driver.close()
            assert False

