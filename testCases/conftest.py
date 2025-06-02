from selenium import webdriver
import pytest
@pytest.fixture()

def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver

def pytest_addoption(parser):  #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")



# PyTest HTML report #

# # it is hook for adding environment info to HTML reports
# def pytest_configure(config):
#     config._metadata['Project Name']= 'nop Commerce'
#     config._metadata['Module Name']='Customers'
#     config._metadata['Tester']='Tejal'

# def pytest_html_report_title(report):
#     report.title = "nopCommerce Test Report"
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([
#         "Project Name: nop Commerce",
#         "Module Name: Login",
#         "Tester: Your Name"
#     ])


# # It is hook for adding environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home", None)
#     metadata.pop("Plugins", None)
