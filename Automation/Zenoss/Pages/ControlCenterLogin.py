from gettext import find
from symbol import return_stmt
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from Automation.Framework.Page import Page
from Automation.Framework.PageFactory import PageFactory
from Automation.Zenoss.Pages.ControlCenterApplications import ControlCenterApplications

__author__ = 'Oscar Mario'


class ControlCenterLogin(Page):
    
    Find_user = (By.XPATH, ".//*[@id='login']/input[1]")
    Find_passwd = (By.XPATH, ".//*[@id='login']/input[2]")
    Find_btnLogin = (By.XPATH, ".//*[@id='login']/button")

    @FindBy ()

    def loginWithValidUser(self):
        self.Find_user.send_keys("zenny")
        self.Find_passwd.send_keys("Z3n0ss")
        return self.go_To_Page(self.Find_btnLogin, ControlCenterApplications())