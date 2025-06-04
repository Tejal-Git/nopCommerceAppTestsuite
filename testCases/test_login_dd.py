import webbrowser

from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
import time
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from time import sleep
from selenium.webdriver.common.by import By
from utilities import XLUtility



class Test_002_DDT_Login:
    baseURL= Readconfig.getApplicationURL()
    path= ".//TestData/testdata.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("Test_002_DDT_Login")
        self.logger.info("Verifying DDT Login test")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtility.getRowCount(self.path, 'Sheet1')
        print("Number of rows in a excel:", self.rows)

        lst_status = [] #empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtility.readData(self.path, 'Sheet1', r,1)
            self.password=XLUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLUtility.readData(self.path,'Sheet1', r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title= self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='pass':
                    self.logger.info("passed")
                    self.lp.clickLogout();
                    lst_status.append("pass")
                elif self.exp=='fail':
                    self.logger.info("failed")
                    self.lp.clickLogout();
                    lst_status.append("fail")
            if act_title != exp_title:
                if self.exp=='pass':
                    self.logger.info("failed")
                    self.lp.clickLogout();
                    lst_status.append("fail")
                elif self.exp=='fail':
                    self.logger.info("passed")
                    self.lp.clickLogout();
                    lst_status.append("pass")

        if 'fail' not in lst_status:
                self.logger.info("Test_002_DDT_Login is passed")
                self.driver.close()
                assert True
        else:
                self.logger.info("Test_002_DDT_Login is failed")
                self.driver.close()
                assert False

        self.logger.info("end of the login DDT test")
        self.logger.info("Test_002_DDT_Login completed")



webbrowser.open("report.html")