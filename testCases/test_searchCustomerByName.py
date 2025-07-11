import time
import pytest
from pageObject.LoginPage import LoginPage
from pageObject.AddcustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("SearchCustomerByName_005")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successful")

        self.logger.info("Starting Search Customer By Name")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("searching customer by Name")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("TC_SearchCustomerByName_005 Finished")