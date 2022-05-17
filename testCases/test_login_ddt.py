import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import Loggen
from utilities import Excelutils
import time

class Test_001_Login_DDT:
    baseURL = readConfig.getApplicationURL()
    path = ".\\TestData\LoginData.xlsx"


    # username = readConfig.getUseremail()
    # password = readConfig.getPassword()

    logger = Loggen.loggen()

    # def test_HomePageTitle(self, setup):
    #     self.logger.info("**************************** test_HomePageTitle initializing ********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #
    #     if act_title == "Your store. Login":
    #         assert True
    #         self.logger.info("*************************** test_HomePageTitle Test Case Passed ********************************")
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+ "test_HomePageTitle.png")
    #         self.logger.error("*************************** test_HomePageTitle Test Case Failed ********************************")
    #         self.driver.close()
    #         assert False


    def test_Login(self, setup):
        self.logger.info("**************************** test_Login initializing ********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = Excelutils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows = ", self.rows)

        lst_status = []

        for r in range (2,self.rows+1):
            self.username = Excelutils.readData(self.path, 'Sheet1', r, 1)
            self.password = Excelutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = Excelutils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
               if self.exp == 'Pass':
                   self.logger.info("************Passsed***********")
                   lst_status.append("Pass")
               else:
                   self.exp== 'Fail'
                   self.logger.info("************Failed***********")
                   lst_status.append("Fail")
            else:
                act_title != exp_title
                if self.exp == "Pass":
                    self.logger.info("*******Failed ***************")
                    lst_status.append("Fail")
                else:
                    self.exp == "Fail"
                    self.logger.info("**********Passed******************")
                    lst_status.append("Pass")

        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("***********Test Case Passed ******************")
            self.driver.close()
            assert True

        else:
            self.logger.info("***********Test Case failed ******************")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")





