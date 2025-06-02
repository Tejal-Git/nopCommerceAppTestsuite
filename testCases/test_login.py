import webbrowser

from selenium import webdriver
import pytest
from pageObject.LoginPage import LoginPage
import time
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from time import sleep
from selenium.webdriver.common.by import By



class Test_001_Login:
    baseURL= Readconfig.getApplicationURL()
    username= Readconfig.getUsername()
    password= Readconfig.getpassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("Test_001_Login")
        self.logger.info("Verifying Home Page Title")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title=self.driver.title
        # print(act_title)
        if act_title== "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home page title test is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Home page title test is failed")
            assert False


    def test_login(self,setup):
        self.logger.info("Verifying Login test")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.driver.find_element(By.XPATH, "//*[@id='wBIvQ7']/div/label/input").click()
        # time.sleep(10)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("Login test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.driver.error("Login test failed")
            assert False

webbrowser.open("report.html")